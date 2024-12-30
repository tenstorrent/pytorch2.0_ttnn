### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                   | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                   | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[]> other = ?                                       | None     | Unknown    | N/A                   | N/A    |
|   2 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.999999051397712     | 0      |
|   3 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999962021489791    | 0      |
|   4 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999960429856729    | 0      |
|   5 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999964573752833    | 0      |
|   6 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999951456371429    | 0      |
|   7 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999998309824559    | 0      |
|   8 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|   9 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  10 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999954475007958    | 0      |
|  11 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.9999951624283371    | 0      |
|  12 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999960714705258    | 0      |
|  13 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|  14 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  15 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999967736237143    | 0      |
|  16 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999998620983801    | 0      |
|  17 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999985269376311    | 0      |
|  18 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999984310105321    | 0      |
|  19 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999923011809343    | 0      |
|  20 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.999996064851178     | 0      |
|  21 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999970238509346    | 0      |
|  22 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999971190917375    | 0      |
|  23 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                   | N/A    |
|  24 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
|  25 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  26 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                   | 0      |
|  27 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953725751722    | 0      |
|  28 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                   | 0      |
|  29 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  30 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972843653071    | 0      |
|  31 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999958630299138    | 0      |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999965264755802    | 0      |
|  33 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999957765824431    | 0      |
|  34 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999952037236105    | 0      |
|  35 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999955660838924    | 0      |
|  36 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.999996625690506     | 0      |
|  37 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952509106373    | 0      |
|  38 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  39 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999974070328317    | 0      |
|  40 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999959715460343    | 0      |
|  41 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.999999402345023     | 0      |
|  42 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999998832666275    | 0      |
|  43 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999984517239993    | 0      |
|  44 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953709250236    | 0      |
|  45 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  46 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971612755045    | 0      |
|  47 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.999996007373833     | 0      |
|  48 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.9999985635463782    | 0      |
|  49 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999960316577459    | 0      |
|  50 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999964909610654    | 0      |
|  51 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.9999956779919446    | 0      |
|  52 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999963424352916    | 0      |
|  53 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999963552106568    | 0      |
|  54 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999952679001072    | 0      |
|  55 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.999996708323541     | 0      |
|  56 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999964438406752    | 0      |
|  57 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999965518328022    | 0      |
|  58 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999959660898752    | 0      |
|  59 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.9999958796343195    | 0      |
|  60 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999960143072575    | 0      |
|  61 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999960283126013    | 0      |
|  62 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999959934566104    | 0      |
|  63 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.9999960231540819    | 0      |
|  64 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999999990400247    | 0      |
|  65 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954743731703    | 0      |
|  66 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  67 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971375947515    | 0      |
|  68 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999958614731864    | 0      |
|  69 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
|  70 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999958052257452    | 0      |
|  71 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999958386829382    | 0      |
|  72 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Done     | Done       | 0.9999961626786762    | 0      |
|  73 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.9999962328084213    | 0      |
|  74 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999958916893886    | 0      |
|  75 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999959733369221    | 0      |
|  76 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | Done       | 0.9999966309563775    | 0      |
|  77 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999960255990176    | 0      |
|  78 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999957702911975    | 0      |
|  79 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999961330180186    | 0      |
|  80 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999960695868834    | 0      |
|  81 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999958738049923    | 0      |
|  82 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999954090379873    | 0      |
|  83 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  84 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972059012409    | 0      |
|  85 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999960337972549    | 0      |
|  86 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999959480854727    | 0      |
|  87 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999961295677192    | 0      |
|  88 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999953219819373    | 0      |
|  89 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
|  90 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.999997160652243     | 0      |
|  91 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999958175535627    | 0      |
|  92 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.999995781575676     | 0      |
|  93 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999958943161487    | 0      |
|  94 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999951579333873    | 0      |
|  95 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
|  96 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                   | 0      |
|  97 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999967092284769    | 0      |
|  98 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999959714459824    | 0      |
|  99 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | 1.0                   | 0      |
| 100 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | Done       | 1.0                   | 0      |
| 101 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999952486478741    | 0      |
| 102 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999959030097816    | 0      |
| 103 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999986770739931    | 0      |
| 104 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Done     | Done       | 0.9999959628161144    | 0      |
| 105 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Done     | Done       | 0.9999959189003808    | 0      |
| 106 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999960685836233    | 0      |
| 107 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Done     | Done       | 0.9999959922848378    | 0      |
| 108 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Done       | 0.9999959291925459    | 0      |
| 109 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 110 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Unknown  | Done       | 0.9999954112073149    | 0      |
| 111 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Unknown  | Done       | 0.9999950081309795    | 0      |
| 112 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999959803762347    | 0      |
| 113 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Done       | 0.9999959492008584    | 0      |
| 114 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | Done       | 0.9999963540856983    | 0      |
| 115 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999958355475304    | 0      |
| 116 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.9999959368853902    | 0      |
| 117 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999963558238497    | 0      |
| 118 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.9999958848011489    | 0      |
| 119 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999958320327215    | 0      |
| 120 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999957397472662    | 0      |
| 121 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.9999961352506891    | 0      |
| 122 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958765917185    | 0      |
| 123 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
| 124 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999962104700062    | 0      |
| 125 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | 0      |
| 126 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999959472199811    | 0      |
| 127 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.9999959710096091    | 0      |
| 128 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | Done       | 0.9999960800067097    | 0      |
| 129 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999957854194542    | 0      |
| 130 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                   | N/A    |
| 131 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.999995894766719     | 0      |
| 132 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.999995644890051     | 0      |
| 133 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999957671832428    | 0      |
| 134 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999957006593055    | 0      |
| 135 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999960218480269    | 0      |
| 136 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999959514639948    | 0      |
| 137 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999959367778298    | 0      |
| 138 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999955682171893    | 0      |
| 139 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959654559585    | 0      |
| 140 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999957982168706    | 0      |
| 141 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.9999958518028234    | 0      |
| 142 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959688528403    | 0      |
| 143 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Removed  | Unknown    | N/A                   | N/A    |
| 144 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Removed  | Done       | 0.9999961891775675    | 0      |
| 145 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Removed  | Done       | 0.9999959625517871    | 0      |
| 146 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Removed  | Unknown    | N/A                   | N/A    |
| 147 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Removed  | Done       | 0.9999960060361722    | 0      |
| 148 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Removed  | Done       | 0.9999960976808546    | 0      |
| 149 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 150 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?                        | Removed  | Unknown    | N/A                   | N/A    |
| 151 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Removed  | Done       | 0.9999959357761573    | 0      |
| 152 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Removed  | Done       | 0.9999959683692647    | 0      |
| 153 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999958042622572    | 0      |
| 154 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959679445958    | 0      |
| 155 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953583691468    | 0      |
| 156 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 157 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999972494142206    | 0      |
| 158 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959591004015    | 0      |
| 159 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
| 160 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999957287821081    | 0      |
| 161 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.999996028499847     | 0      |
| 162 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.999998353286036     | 0      |
| 163 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999959347109568    | 0      |
| 164 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.9999959301648498    | 0      |
| 165 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 166 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959395448531    | 0      |
| 167 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999953900182593    | 0      |
| 168 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999961619789131    | 0      |
| 169 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999958220971269    | 0      |
| 170 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.999995334065943     | 0      |
| 171 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
| 172 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999971965079818    | 0      |
| 173 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999959109714351    | 0      |
| 174 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.9999969978195457    | 0      |
| 175 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Done     | Done       | 0.999996119832413     | 0      |
| 176 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.999995762259177     | 0      |
| 177 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Done     | Done       | 0.9999959773140656    | 0      |
| 178 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.999995923252977     | 0      |
| 179 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999960324850375    | 0      |
| 180 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999961432430964    | 0      |
| 181 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999954048015658    | 0      |
| 182 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
| 183 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999972786683864    | 0      |
| 184 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999960389736103    | 0      |
| 185 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999960131013788    | 0      |
| 186 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.999995903676594     | 0      |
| 187 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | 0      |
| 188 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | Done       | 0.9999971507489703    | 0      |
| 189 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Done     | Done       | 0.9999959639308426    | 0      |
| 190 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Done     | Done       | 0.9999960441669792    | 0      |
| 191 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.999995957888819     | 0      |
| 192 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999961319982164    | 0      |
| 193 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960409951952    | 0      |
| 194 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959849892451    | 0      |
| 195 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999957717792863    | 0      |
| 196 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999960461055162    | 0      |
| 197 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999959700935884    | 0      |
| 198 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Unknown  | Done       | 0.9999972233753234    | 0      |
| 199 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999959762509547    | 0      |
| 200 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999958689451871    | 0      |
| 201 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999957888142674    | 0      |
| 202 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                   | 0      |
| 203 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.9999980087264796    | 0      |
| 204 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 205 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999942573524626    | 0      |
| 206 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | Done       | 0.9999984630966429    | 0      |
| 207 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.999996508927362     | 0      |
| 208 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 209 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.999995891418449     | 0      |
| 210 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999959750858154    | 0      |
| 211 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999961415925107    | 0      |
| 212 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999959649289835    | 0      |
| 213 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999962719596235    | 0      |
| 214 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 215 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.9999960776682317    | 0      |
| 216 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.9999959572645789    | 0      |
| 217 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 218 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999958748132834    | 0      |
| 219 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999966149318497    | 0      |
| 220 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999959431262909    | 0      |
| 221 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999959629941291    | 0      |
| 222 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999959965845276    | 0      |
| 223 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 224 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999958816940115    | 0      |
| 225 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999960683309779    | 0      |
| 226 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 227 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999958677033816    | 0      |
| 228 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999963837068726    | 0      |
| 229 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.999995833986449     | 0      |
| 230 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Done     | Done       | 0.9999959342594289    | 0      |
| 231 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999960673838246    | 0      |
| 232 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Done     | Done       | 0.9999959733000642    | 0      |
| 233 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999958241681427    | 0      |
| 234 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999958994861537    | 0      |
| 235 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999960029462229    | 0      |
| 236 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999958876664286    | 0      |
| 237 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999957384547151    | 0      |
| 238 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999959619265136    | 0      |
| 239 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954780435967    | 0      |
| 240 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 241 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972337726524    | 0      |
| 242 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999960242615623    | 0      |
| 243 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999960111509867    | 0      |
| 244 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Done     | Done       | 0.9999961115678372    | 0      |
| 245 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999957429721682    | 0      |
| 246 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999959256736974    | 0      |
| 247 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999957552472033    | 0      |
| 248 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999958929595932    | 0      |
| 249 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999958805678606    | 0      |
| 250 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999959538106004    | 0      |
| 251 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999960036120868    | 0      |
| 252 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.9999962079304413    | 0      |
| 253 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 254 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999958753801238    | 0      |
| 255 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Done       | 0.9999961305027016    | 0      |
| 256 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999948942985212    | 0      |
| 257 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                   | 0      |
| 258 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999971534505144    | 0      |
| 259 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999962414630212    | 0      |
| 260 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953287764938    | 0      |
| 261 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 262 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972108090668    | 0      |
| 263 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999958537666181    | 0      |
| 264 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953813772254    | 0      |
| 265 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 266 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971806441276    | 0      |
| 267 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999959977770383    | 0      |
| 268 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.999995308312857     | 0      |
| 269 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 270 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972171687509    | 0      |
| 271 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999961537772136    | 0      |
| 272 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.999995432568383     | 0      |
| 273 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 274 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972087749639    | 0      |
| 275 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999960152879762    | 0      |
| 276 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999964945740861    | 0      |
| 277 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999958226527556    | 0      |
| 278 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.9999959465127041    | 0      |
| 279 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.999996009320941     | 0      |
| 280 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 281 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 282 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 283 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 284 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 285 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                   | N/A    |
| 286 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 287 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 288 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999970837901663    | 0      |
| 289 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999962139164996    | 0      |
| 290 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | Done       | 0.9999959856373838    | 0      |
| 291 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 292 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 293 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958393750057    | 0      |
| 294 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | 0.06288200027282081   | 0      |
| 295 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958232508936    | 0      |
| 296 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.13971491988513302   | 0      |
| 297 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 298 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 299 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 300 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 301 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Unknown  | Done       | 1.0                   | 0      |
| 302 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Unknown  | Done       | 0.9999975066571596    | 0      |
| 303 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | Fallback   | 1.0                   | -1     |
| 304 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 305 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Unknown  | Done       | 0.9999962636381333    | 0      |
| 306 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999959246044839    | 0      |
| 307 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999958961690176    | 0      |
| 308 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                   | 0      |
| 309 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                   | 0      |
| 310 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 311 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957621048706    | 0      |
| 312 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.2772497211129271    | 0      |
| 313 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958571165042    | 0      |
| 314 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.3446172134833982    | 0      |
| 315 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999947183971635    | 0      |
| 316 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999960027238471    | 0      |
| 317 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999957740932921    | 0      |
| 318 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958787522655    | 0      |
| 319 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | -0.047607542365861746 | 0      |
| 320 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958878336462    | 0      |
| 321 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | -0.04064679403259114  | 0      |
| 322 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.999996531148345     | 0      |
| 323 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999963705154715    | 0      |
| 324 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | Done       | 0.9999960981674892    | 0      |
| 325 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Done     | Done       | 1.0                   | 0      |
| 326 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Done     | Unknown    | N/A                   | N/A    |
| 327 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | None     | Fallback   | 1.0                   | -1     |
| 328 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 329 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                   | N/A    |

