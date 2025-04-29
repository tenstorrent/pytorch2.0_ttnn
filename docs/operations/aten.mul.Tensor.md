### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                   | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                   | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[8732, 1]> other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
|   2 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999971896910462    | -1     |
|   3 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999963846072492    | -1     |
|   4 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999973419114967    | -1     |
|   5 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999960133122081    | -1     |
|   6 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                   | N/A    |
|   7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                   | N/A    |
|   8 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?             | Done     | Unknown    | N/A                   | N/A    |
|   9 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.999994443961182     | -1     |
|  10 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999994037806017    | -1     |
|  11 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | -1     |
|  12 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                   | -1     |
|  13 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999952019540819    | -1     |
|  14 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.9999951684780052    | -1     |
|  15 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999952540646765    | -1     |
|  16 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | -1     |
|  17 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                   | -1     |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999995259587824    | -1     |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999974418781514    | -1     |
|  20 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999889207533774    | -1     |
|  21 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999998922264491    | -1     |
|  22 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.999996551904954     | -1     |
|  23 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999949713914053    | -1     |
|  24 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.999998686813194     | -1     |
|  25 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999968292619056    | -1     |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                   | N/A    |
|  27 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
|  28 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                   | -1     |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999955729727924    | -1     |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                   | -1     |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | -1     |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999970678194269    | -1     |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999959622385985    | -1     |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999960873095263    | -1     |
|  36 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                   | N/A    |
|  37 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                   | N/A    |
|  38 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?             | Done     | Unknown    | N/A                   | N/A    |
|  39 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999961871808151    | -1     |
|  40 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.999995140716629     | -1     |
|  41 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999955481349964    | -1     |
|  42 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999966174869666    | -1     |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953422893954    | -1     |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | -1     |
|  45 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972192776586    | -1     |
|  46 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999955787189087    | -1     |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999995907768567    | -1     |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999964994025622    | -1     |
|  49 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999992540069538    | -1     |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999949801499601    | -1     |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | -1     |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999974572448128    | -1     |
|  53 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999957674860793    | -1     |
|  54 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Unknown  | Done       | 0.9999985410141387    | -1     |
|  55 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999951246434653    | -1     |
|  56 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999955446827385    | -1     |
|  57 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.999995550776542     | -1     |
|  58 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999948334944421    | -1     |
|  59 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999964499141747    | -1     |
|  60 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999958077690518    | -1     |
|  61 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999972014121454    | -1     |
|  62 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Unknown  | Done       | 0.9999964741093094    | -1     |
|  63 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999946895685832    | -1     |
|  64 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Unknown  | Done       | 0.9999960186710788    | -1     |
|  65 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999960143554606    | -1     |
|  66 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999961276955938    | -1     |
|  67 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999959880495287    | -1     |
|  68 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999959751041171    | -1     |
|  69 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999979384867522    | -1     |
|  70 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953623960767    | -1     |
|  71 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | -1     |
|  72 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971236669631    | -1     |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999961774583642    | -1     |
|  74 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | -1     |
|  75 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999959806877605    | -1     |
|  76 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999963393363726    | -1     |
|  77 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999961126065846    | -1     |
|  78 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.9999960335256203    | -1     |
|  79 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999958198518761    | -1     |
|  80 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999960717699068    | -1     |
|  81 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Unknown  | Done       | 0.9999980997622655    | -1     |
|  82 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | 0.9999958103817194    | -1     |
|  83 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Unknown  | Done       | 0.9999959274313901    | -1     |
|  84 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999959781254709    | -1     |
|  85 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.999995365125057     | -1     |
|  86 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | -1     |
|  87 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972160413858    | -1     |
|  88 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999958545054919    | -1     |
|  89 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999958193829673    | -1     |
|  90 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999959182581466    | -1     |
|  91 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.999995251975537     | -1     |
|  92 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | -1     |
|  93 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971889115147    | -1     |
|  94 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999956259740802    | -1     |
|  95 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.9999962897134351    | -1     |
|  96 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999959538003851    | -1     |
|  97 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999956924594091    | -1     |
|  98 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | -1     |
|  99 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 1.0                   | -1     |
| 100 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999985401913906    | -1     |
| 101 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999958130824976    | -1     |
| 102 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | 1.0                   | -1     |
| 103 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | Done       | 1.0                   | -1     |
| 104 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999956454726232    | -1     |
| 105 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999956557490302    | -1     |
| 106 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | -1     |
| 107 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Done     | Done       | 1.0                   | -1     |
| 108 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | Done       | 0.9999952647860634    | -1     |
| 109 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999959471185954    | -1     |
| 110 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999958923278475    | -1     |
| 111 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Unknown  | Done       | 0.999995813093563     | -1     |
| 112 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Unknown  | Done       | 0.9999959730720847    | -1     |
| 113 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999958908332659    | -1     |
| 114 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999961125179676    | -1     |
| 115 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999958919110757    | -1     |
| 116 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Unknown  | Done       | 0.9999953865234       | -1     |
| 117 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999961632339993    | -1     |
| 118 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958271475196    | -1     |
| 119 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | -1     |
| 120 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999954265724704    | -1     |
| 121 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | -1     |
| 122 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999958954071807    | -1     |
| 123 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999959462091521    | -1     |
| 124 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Unknown  | Done       | 0.9999952958946076    | -1     |
| 125 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                   | N/A    |
| 126 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999959093172496    | -1     |
| 127 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.999995963719289     | -1     |
| 128 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.9999959156805309    | -1     |
| 129 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999971267576704    | -1     |
| 130 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  | Done       | 0.9999959922981173    | -1     |
| 131 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999957975025806    | -1     |
| 132 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959873892691    | -1     |
| 133 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Unknown  | Done       | 0.9999958329840434    | -1     |
| 134 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Unknown    | N/A                   | N/A    |
| 135 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999961389920611    | -1     |
| 136 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.999995914622944     | -1     |
| 137 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Unknown  | Unknown    | N/A                   | N/A    |
| 138 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  | Done       | 0.9999957696289035    | -1     |
| 139 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Unknown  | Done       | 0.9999959905987238    | -1     |
| 140 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                   | N/A    |
| 141 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999960522340784    | -1     |
| 142 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | 0.9999960395543342    | -1     |
| 143 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | -1     |
| 144 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999959117241634    | -1     |
| 145 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957617682852    | -1     |
| 146 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953600371349    | -1     |
| 147 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | -1     |
| 148 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999972252748552    | -1     |
| 149 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959995395584    | -1     |
| 150 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | -1     |
| 151 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999960882341649    | -1     |
| 152 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.999996028160137     | -1     |
| 153 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999957507219048    | -1     |
| 154 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999960778599061    | -1     |
| 155 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999960115094683    | -1     |
| 156 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | -1     |
| 157 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999953832702937    | -1     |
| 158 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999958751847586    | -1     |
| 159 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999959339076577    | -1     |
| 160 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999954139704779    | -1     |
| 161 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | -1     |
| 162 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999972011682282    | -1     |
| 163 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959716077563    | -1     |
| 164 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999962320262967    | -1     |
| 165 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.9999961401851987    | -1     |
| 166 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999959423052645    | -1     |
| 167 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999957843185382    | -1     |
| 168 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999959552779413    | -1     |
| 169 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999959381208032    | -1     |
| 170 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999967062885667    | -1     |
| 171 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952733055442    | -1     |
| 172 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | -1     |
| 173 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971879083767    | -1     |
| 174 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999956213576233    | -1     |
| 175 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999959919037201    | -1     |
| 176 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999959748370543    | -1     |
| 177 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | -1     |
| 178 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Unknown  | Done       | 0.9999949974865063    | -1     |
| 179 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Unknown  | Done       | 0.9999958825155075    | -1     |
| 180 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | 0.9999959068780919    | -1     |
| 181 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999957824827912    | -1     |
| 182 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959563597565    | -1     |
| 183 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | 0.9999959087725272    | -1     |
| 184 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Unknown  | Done       | 0.9999958429898722    | -1     |
| 185 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | Done       | 0.9999960957300724    | -1     |
| 186 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.999995786565132     | -1     |
| 187 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999958719610691    | -1     |
| 188 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999959591434865    | -1     |
| 189 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                   | -1     |
| 190 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999984721081202    | -1     |
| 191 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | -1     |
| 192 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999968472372903    | -1     |
| 193 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Unknown  | Done       | 0.9999988231345261    | -1     |
| 194 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999964619573207    | -1     |
| 195 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 196 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Unknown  | Done       | 0.9999959297087654    | -1     |
| 197 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Unknown  | Done       | 0.9999960400350051    | -1     |
| 198 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Unknown  | Done       | 0.9999961790071389    | -1     |
| 199 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | 0.9999956862989751    | -1     |
| 200 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 201 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Unknown  | Done       | 0.9999959841330044    | -1     |
| 202 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Unknown  | Done       | 0.9999960787633952    | -1     |
| 203 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Unknown  | Unknown    | N/A                   | N/A    |
| 204 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Unknown  | Done       | 0.999995851467917     | -1     |
| 205 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Unknown  | Done       | 0.9999957266923334    | -1     |
| 206 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Unknown  | Done       | 0.9999960067639744    | -1     |
| 207 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | 0.9999955987006274    | -1     |
| 208 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 209 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Unknown  | Done       | 0.9999959668913875    | -1     |
| 210 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Unknown  | Done       | 0.9999959133824085    | -1     |
| 211 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Unknown  | Unknown    | N/A                   | N/A    |
| 212 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Unknown  | Done       | 0.9999960181388737    | -1     |
| 213 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Unknown  | Done       | 0.9999954908806775    | -1     |
| 214 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Unknown  | Done       | 0.9999961008527002    | -1     |
| 215 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999959027919589    | -1     |
| 216 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999959787295871    | -1     |
| 217 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.999996041817639     | -1     |
| 218 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.999995956784975     | -1     |
| 219 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999959682988776    | -1     |
| 220 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999959790288667    | -1     |
| 221 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999959068006851    | -1     |
| 222 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999959947564818    | -1     |
| 223 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999960663849597    | -1     |
| 224 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954684174212    | -1     |
| 225 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | -1     |
| 226 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971967694518    | -1     |
| 227 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999958361038911    | -1     |
| 228 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999957024294535    | -1     |
| 229 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999961954507859    | -1     |
| 230 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999959915727114    | -1     |
| 231 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999964448911842    | -1     |
| 232 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999957530791606    | -1     |
| 233 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999959165673836    | -1     |
| 234 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999959317931483    | -1     |
| 235 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999961353516509    | -1     |
| 236 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999959205996248    | -1     |
| 237 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?          | Done     | Unknown    | N/A                   | N/A    |
| 238 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?          | Done     | Unknown    | N/A                   | N/A    |
| 239 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.9999962086474435    | -1     |
| 240 | Tensor<[1, 7]> self = ?,<br>Tensor other = ?                                   | Done     | Unknown    | N/A                   | N/A    |
| 241 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | -1     |
| 242 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999959594613193    | -1     |
| 243 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.9999960379449823    | -1     |
| 244 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999957639518108    | -1     |
| 245 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                   | -1     |
| 246 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999971103237385    | -1     |
| 247 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999961257415       | -1     |
| 248 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954040670315    | -1     |
| 249 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | -1     |
| 250 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972199246636    | -1     |
| 251 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999959671265403    | -1     |
| 252 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.999995389137692     | -1     |
| 253 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | -1     |
| 254 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971860502729    | -1     |
| 255 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999958390681786    | -1     |
| 256 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.999995349575836     | -1     |
| 257 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | -1     |
| 258 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971371223938    | -1     |
| 259 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.999996006281296     | -1     |
| 260 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953810572254    | -1     |
| 261 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | -1     |
| 262 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971496673724    | -1     |
| 263 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999958396739693    | -1     |
| 264 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.999995599532791     | -1     |
| 265 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999957997595478    | -1     |
| 266 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.9999960942535254    | -1     |
| 267 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999960430759144    | -1     |
| 268 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                   | N/A    |
| 269 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | -1     |
| 270 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | -1     |
| 271 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999967972915682    | -1     |
| 272 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999961795728844    | -1     |
| 273 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | -1     |
| 274 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | -1     |
| 275 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959148818457    | -1     |
| 276 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.0041945241975474175 | -1     |
| 277 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958686150854    | -1     |
| 278 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | -0.004359744950409593 | -1     |
| 279 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | -1     |
| 280 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | Done       | 1.0                   | -1     |
| 281 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | Done       | 0.9999946231399857    | -1     |
| 282 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | Done     | Done       | 1.0                   | -1     |
| 283 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | -1     |
| 284 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | Done       | 0.9999959092366372    | -1     |
| 285 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999959075813287    | -1     |
| 286 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999958075285622    | -1     |
| 287 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                   | -1     |
| 288 | Tensor<[200]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
| 289 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                   | -1     |
| 290 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 291 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959278834514    | -1     |
| 292 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.07072747766207813   | -1     |
| 293 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958441760142    | -1     |
| 294 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.2096298575706396    | -1     |
| 295 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.999994486470317     | -1     |
| 296 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999957606890493    | -1     |
| 297 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.999995988694363     | -1     |
| 298 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958581482403    | -1     |
| 299 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | -0.014606285674904228 | -1     |
| 300 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958462094318    | -1     |
| 301 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | 0.006756135154006203  | -1     |
| 302 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.9999958502810531    | -1     |
| 303 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999958091344773    | -1     |
| 304 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Unknown  | Unknown    | N/A                   | N/A    |
| 305 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Unknown  | Done       | 1.0                   | -1     |
| 306 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
| 307 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Unknown    | N/A                   | N/A    |
| 308 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Done     | Done       | 0.9999960738940223    | -1     |
| 309 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Done     | Done       | 1.0                   | -1     |
| 310 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                   | N/A    |

