### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                  | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:---------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                  | N/A    |
|   1 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999993732911755   | 0      |
|   2 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999970551380417   | 0      |
|   3 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.999996573356322    | 0      |
|   4 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999951085576546   | 0      |
|   5 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                  | N/A    |
|   6 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                  | N/A    |
|   7 | Tensor<[1, 1, 1, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?             | Done     | Unknown    | N/A                  | N/A    |
|   8 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999973613221163   | 0      |
|   9 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999994050553365   | 0      |
|  10 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                  | 0      |
|  11 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                  | 0      |
|  12 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999953796201911   | 0      |
|  13 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999957259975868   | 0      |
|  14 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                  | 0      |
|  15 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                  | 0      |
|  16 | Tensor<[1, 1, 1, 384]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Unknown    | N/A                  | N/A    |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999972540230608   | 0      |
|  18 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999991647090042   | 0      |
|  19 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999943808698294   | 0      |
|  20 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999975776246403   | 0      |
|  21 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999988401062931   | 0      |
|  22 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999983361375254   | 0      |
|  23 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999961900727112   | 0      |
|  24 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.999995525468266    | 0      |
|  25 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                  | N/A    |
|  26 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                  | N/A    |
|  27 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                  | N/A    |
|  28 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                  | 0      |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999944810941491   | 0      |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                  | 0      |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                  | 0      |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.999997204083732    | 0      |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999961052816204   | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999947929952013   | 0      |
|  35 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Unknown    | N/A                  | N/A    |
|  36 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Unknown    | N/A                  | N/A    |
|  37 | Tensor<[1, 1, 16, 1]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?             | Done     | Unknown    | N/A                  | N/A    |
|  38 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999966627499003   | 0      |
|  39 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999952530093459   | 0      |
|  40 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999955014741305   | 0      |
|  41 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999965041601898   | 0      |
|  42 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 1                              | Unknown  | Unknown    | N/A                  | N/A    |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999954000426541   | 0      |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                  | 0      |
|  45 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971588651733   | 0      |
|  46 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.999996321828825    | 0      |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999985849387395   | 0      |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999966069563012   | 0      |
|  49 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999922085413203   | 0      |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999955081363227   | 0      |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                  | 0      |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999973600047197   | 0      |
|  53 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999961965209847   | 0      |
|  54 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.9999985603417981   | 0      |
|  55 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999957794236323   | 0      |
|  56 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999959933791307   | 0      |
|  57 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.9999961338014519   | 0      |
|  58 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.125                          | Unknown  | Unknown    | N/A                  | N/A    |
|  59 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999965068016851   | 0      |
|  60 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999961488270063   | 0      |
|  61 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999952039198733   | 0      |
|  62 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999953941593865   | 0      |
|  63 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Removed  | Done       | 0.9999968879475765   | 0      |
|  64 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999951449118701   | 0      |
|  65 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999959404081009   | 0      |
|  66 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999961420037012   | 0      |
|  67 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999958961865056   | 0      |
|  68 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999960901818334   | 0      |
|  69 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999959219139182   | 0      |
|  70 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999997816258452   | 0      |
|  71 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953158879907   | 0      |
|  72 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                  | 0      |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971598430177   | 0      |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999959143777996   | 0      |
|  75 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                  | 0      |
|  76 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999961433156089   | 0      |
|  77 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999961466642877   | 0      |
|  78 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999962635558984   | 0      |
|  79 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.9999959262482482   | 0      |
|  80 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999959865985723   | 0      |
|  81 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.999996075073472    | 0      |
|  82 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Removed  | Done       | 0.9999962464051944   | 0      |
|  83 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999955836983581   | 0      |
|  84 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999959521018642   | 0      |
|  85 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999958223680848   | 0      |
|  86 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999952705413266   | 0      |
|  87 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                  | 0      |
|  88 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971763840647   | 0      |
|  89 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999959250766769   | 0      |
|  90 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999959710374274   | 0      |
|  91 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999962895224145   | 0      |
|  92 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999951441283497   | 0      |
|  93 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                  | 0      |
|  94 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971645627681   | 0      |
|  95 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999959389231038   | 0      |
|  96 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.9999966803384215   | 0      |
|  97 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999960571401622   | 0      |
|  98 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999959730131778   | 0      |
|  99 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                  | 0      |
| 100 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Done     | Done       | 1.0                  | 0      |
| 101 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999966007017518   | 0      |
| 102 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999959580920257   | 0      |
| 103 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999966738616036   | 0      |
| 104 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999964988913059   | 0      |
| 105 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                  | 0      |
| 106 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Done     | Done       | 0.9999970692183214   | 0      |
| 107 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Done     | Done       | 0.9999948873605218   | 0      |
| 108 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999958875942889   | 0      |
| 109 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999959031436384   | 0      |
| 110 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Removed  | Done       | 0.9999960572159384   | 0      |
| 111 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999960443159057   | 0      |
| 112 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999961942006564   | 0      |
| 113 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999959384410096   | 0      |
| 114 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999958686940505   | 0      |
| 115 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999960187036218   | 0      |
| 116 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999959701289751   | 0      |
| 117 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958337249236   | 0      |
| 118 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                  | 0      |
| 119 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999961082112967   | 0      |
| 120 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                  | 0      |
| 121 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999959899349066   | 0      |
| 122 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.999995926154668    | 0      |
| 123 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Removed  | Done       | 0.9999960165227354   | 0      |
| 124 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                  | N/A    |
| 125 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999961335672274   | 0      |
| 126 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.9999961099507492   | 0      |
| 127 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999959559362355   | 0      |
| 128 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999958471261211   | 0      |
| 129 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999961238756899   | 0      |
| 130 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999958087065676   | 0      |
| 131 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959447305977   | 0      |
| 132 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999960271868181   | 0      |
| 133 | Tensor<[1, 257, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Unknown    | N/A                  | N/A    |
| 134 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999962884305363   | 0      |
| 135 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959158103866   | 0      |
| 136 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                  | N/A    |
| 137 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Done     | Done       | 0.999996005704462    | 0      |
| 138 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Done     | Done       | 0.9999957626549485   | 0      |
| 139 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Done     | Unknown    | N/A                  | N/A    |
| 140 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Done     | Done       | 0.9999957852406706   | 0      |
| 141 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Done     | Done       | 0.9999959562128226   | 0      |
| 142 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                  | 0      |
| 143 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.999995881864472    | 0      |
| 144 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958317925957   | 0      |
| 145 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954044738822   | 0      |
| 146 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                  | 0      |
| 147 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999972231614006   | 0      |
| 148 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959596933948   | 0      |
| 149 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Removed  | Done       | 1.0                  | 0      |
| 150 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999960033634016   | 0      |
| 151 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.9999958544255657   | 0      |
| 152 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999982233731468   | 0      |
| 153 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999959314084891   | 0      |
| 154 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959272960638   | 0      |
| 155 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                  | 0      |
| 156 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999995099193862   | 0      |
| 157 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999964320465016   | 0      |
| 158 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999959687600529   | 0      |
| 159 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999953490583641   | 0      |
| 160 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                  | 0      |
| 161 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999972023861232   | 0      |
| 162 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959644768235   | 0      |
| 163 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999960945874664   | 0      |
| 164 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.99999583085644     | 0      |
| 165 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999958760026276   | 0      |
| 166 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999960460962121   | 0      |
| 167 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999958473475273   | 0      |
| 168 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999959438506192   | 0      |
| 169 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999960106628848   | 0      |
| 170 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953345368674   | 0      |
| 171 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                  | 0      |
| 172 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972240686745   | 0      |
| 173 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999962244882473   | 0      |
| 174 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999960192180536   | 0      |
| 175 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999959711742573   | 0      |
| 176 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                  | 0      |
| 177 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Removed  | Done       | 0.9999968068631993   | 0      |
| 178 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999957439331986   | 0      |
| 179 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960298989345   | 0      |
| 180 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999962042430688   | 0      |
| 181 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959788042899   | 0      |
| 182 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960153847521   | 0      |
| 183 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999959383410666   | 0      |
| 184 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Done     | Done       | 0.9999945024462837   | 0      |
| 185 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999957632953186   | 0      |
| 186 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999960370330234   | 0      |
| 187 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.999995843167749    | 0      |
| 188 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                  | 0      |
| 189 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999947071515823   | 0      |
| 190 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                  | 0      |
| 191 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999961539567707   | 0      |
| 192 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Removed  | Done       | 0.9999950565770668   | 0      |
| 193 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999959680320499   | 0      |
| 194 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                  | N/A    |
| 195 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959442486699   | 0      |
| 196 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999958591215099   | 0      |
| 197 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999961464476541   | 0      |
| 198 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999960413642969   | 0      |
| 199 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                  | N/A    |
| 200 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999959103598659   | 0      |
| 201 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999959299824904   | 0      |
| 202 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                  | N/A    |
| 203 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999958924257594   | 0      |
| 204 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999956093503217   | 0      |
| 205 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999954094408433   | 0      |
| 206 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999958193242249   | 0      |
| 207 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                  | N/A    |
| 208 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999959124151984   | 0      |
| 209 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999959099524043   | 0      |
| 210 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                  | N/A    |
| 211 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999959259558404   | 0      |
| 212 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999958129841571   | 0      |
| 213 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.9999962645607694   | 0      |
| 214 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999959527035576   | 0      |
| 215 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999959176190819   | 0      |
| 216 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.9999958974935287   | 0      |
| 217 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999959609715545   | 0      |
| 218 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999960329177112   | 0      |
| 219 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999959555096972   | 0      |
| 220 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999958009219951   | 0      |
| 221 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999961043144445   | 0      |
| 222 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999959954724228   | 0      |
| 223 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953179860207   | 0      |
| 224 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                  | 0      |
| 225 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972157871979   | 0      |
| 226 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999960823759908   | 0      |
| 227 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999962516452993   | 0      |
| 228 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999956627477073   | 0      |
| 229 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999956662767865   | 0      |
| 230 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999964257228613   | 0      |
| 231 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999959470075306   | 0      |
| 232 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999958954731777   | 0      |
| 233 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999960079306249   | 0      |
| 234 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999962122229685   | 0      |
| 235 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999959702786957   | 0      |
| 236 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 1, 16]> other = ?          | Done     | Unknown    | N/A                  | N/A    |
| 237 | Tensor<[1, 768, 16, 16]> self = ?,<br>Tensor<[1, 1, 16, 1]> other = ?          | Done     | Unknown    | N/A                  | N/A    |
| 238 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.999995964122799    | 0      |
| 239 | Tensor<[1, 7]> self = ?,<br>Tensor other = ?                                   | Done     | Unknown    | N/A                  | N/A    |
| 240 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Removed  | Done       | 1.0                  | 0      |
| 241 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999956648485574   | 0      |
| 242 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.9999958997201834   | 0      |
| 243 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999955900389383   | 0      |
| 244 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                  | 0      |
| 245 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999973559151634   | 0      |
| 246 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999966722051289   | 0      |
| 247 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.999995372849126    | 0      |
| 248 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                  | 0      |
| 249 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.999997266132283    | 0      |
| 250 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.999996004965297    | 0      |
| 251 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953433589999   | 0      |
| 252 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                  | 0      |
| 253 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999970970399967   | 0      |
| 254 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999958601153098   | 0      |
| 255 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953727378378   | 0      |
| 256 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                  | 0      |
| 257 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971628106338   | 0      |
| 258 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999960672028531   | 0      |
| 259 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.999995370429295    | 0      |
| 260 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                  | 0      |
| 261 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971531300563   | 0      |
| 262 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999958896277261   | 0      |
| 263 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999958337877679   | 0      |
| 264 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999961843246427   | 0      |
| 265 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.999995981159351    | 0      |
| 266 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999960712277999   | 0      |
| 267 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 1                             | Unknown  | Unknown    | N/A                  | N/A    |
| 268 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                  | N/A    |
| 269 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                  | 0      |
| 270 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                  | 0      |
| 271 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999955180198468   | 0      |
| 272 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999956523679449   | 0      |
| 273 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                  | 0      |
| 274 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                  | 0      |
| 275 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958649477897   | 0      |
| 276 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.07317057821858562  | 0      |
| 277 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958272505843   | 0      |
| 278 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.15007904690866566  | 0      |
| 279 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                  | 0      |
| 280 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Done     | Done       | 1.0                  | 0      |
| 281 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Done     | Done       | 0.9999946570833165   | 0      |
| 282 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | Done     | Done       | 1.0                  | 0      |
| 283 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                  | 0      |
| 284 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Done     | Done       | 0.9999954050582612   | 0      |
| 285 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999960469409199   | 0      |
| 286 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999960101629656   | 0      |
| 287 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                  | 0      |
| 288 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                  | 0      |
| 289 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                  | N/A    |
| 290 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957976888092   | 0      |
| 291 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.3701321031399355   | 0      |
| 292 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958844163062   | 0      |
| 293 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.09756561396604749  | 0      |
| 294 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999966463765841   | 0      |
| 295 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999960733306147   | 0      |
| 296 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999957435575971   | 0      |
| 297 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.999995849387023    | 0      |
| 298 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.027699647512804654 | 0      |
| 299 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958298549848   | 0      |
| 300 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | -0.03626888681546312 | 0      |
| 301 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.999996266944347    | 0      |
| 302 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999959929327273   | 0      |
| 303 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                  | 0      |
| 304 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                  | N/A    |
| 305 | Tensor<[]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                          | Unknown  | Unknown    | N/A                  | N/A    |
| 306 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | Unknown  | Done       | 0.9999954361053258   | 0      |
| 307 | Tensor<[]> self = ?,<br>Tensor<[1, s0, 768]> other = ?                         | Unknown  | Unknown    | N/A                  | N/A    |
| 308 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Done     | Done       | 1.0                  | 0      |
| 309 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                  | N/A    |

