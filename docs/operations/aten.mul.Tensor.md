### aten.mul.Tensor
|     | ATen Input Variations                                                          | Status   | Isolated   | PCC                   | Host   |
|----:|:-------------------------------------------------------------------------------|:---------|:-----------|:----------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor<[0, 1]> other = ?                                   | Unknown  | Unknown    | N/A                   | N/A    |
|   1 | Tensor self = ?,<br>Tensor<[1, 1, 32]> other = ?                               | Done     | Unknown    | N/A                   | N/A    |
|   2 | Tensor self = ?,<br>Tensor<[3234, 1]> other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
|   3 | Tensor self = ?,<br>Tensor<[8732, 1]> other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
|   4 | Tensor self = ?,<br>Tensor<[]> other = ?                                       | Unknown  | Unknown    | N/A                   | N/A    |
|   5 | Tensor<[0, 1]> self = ?,<br>Tensor<[0, 1]> other = ?                           | Unknown  | Done       | 1.0                   | 0      |
|   6 | Tensor<[0]> self = ?,<br>Tensor other = 0.5                                    | Unknown  | Done       | 1.0                   | 0      |
|   7 | Tensor<[0]> self = ?,<br>Tensor<[]> other = ?                                  | Unknown  | Fallback   | 1.0                   | -1     |
|   8 | Tensor<[1, 1, 1, 10]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999950733278652    | 0      |
|   9 | Tensor<[1, 1, 1, 12]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999963335051245    | 0      |
|  10 | Tensor<[1, 1, 1, 14]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999953314116535    | 0      |
|  11 | Tensor<[1, 1, 1, 15]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999960515809297    | 0      |
|  12 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Unknown  | Done       | 0.9999960123903727    | 0      |
|  13 | Tensor<[1, 1, 1, 17]> self = ?,<br>Tensor<[1, 1, 1, 17]> other = ?             | Unknown  | Done       | 0.9999994766054715    | 0      |
|  14 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|  15 | Tensor<[1, 1, 1, 1]> self = ?,<br>Tensor<[1, 1, 1, 1]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  16 | Tensor<[1, 1, 1, 2048]> self = ?,<br>Tensor other = -3.3895313892515355e+38    | Done     | Done       | 0.9999954184784464    | 0      |
|  17 | Tensor<[1, 1, 1, 256]> self = ?,<br>Tensor other = -3.3895313892515355e+38     | Done     | Done       | 0.999995235573696     | 0      |
|  18 | Tensor<[1, 1, 1, 25]> self = ?,<br>Tensor other = -3.3895313892515355e+38      | Done     | Done       | 0.9999952433789933    | 0      |
|  19 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 1.0                   | 0      |
|  20 | Tensor<[1, 1, 1, 2]> self = ?,<br>Tensor<[1, 1, 1, 2]> other = ?               | Unknown  | Done       | 1.0                   | 0      |
|  21 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999976960524544    | 0      |
|  22 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999998364488764    | 0      |
|  23 | Tensor<[1, 1, 1, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?             | Done     | Done       | 0.9999994004053268    | 0      |
|  24 | Tensor<[1, 1, 1, 5]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999984077726495    | 0      |
|  25 | Tensor<[1, 1, 1, 6]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Unknown  | Done       | 0.9999963300777684    | 0      |
|  26 | Tensor<[1, 1, 1, 7]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999972587249277    | 0      |
|  27 | Tensor<[1, 1, 1, 8]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.999996502092655     | 0      |
|  28 | Tensor<[1, 1, 1, 9]> self = ?,<br>Tensor other = -3.3895313892515355e+38       | Done     | Done       | 0.9999941249822858    | 0      |
|  29 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38  | Unknown  | Unknown    | N/A                   | N/A    |
|  30 | Tensor<[1, 1, 1, s0 + 1]> self = ?,<br>Tensor<[1, 1, 1, s0 + 1]> other = ?     | Unknown  | Unknown    | N/A                   | N/A    |
|  31 | Tensor<[1, 1, 1, s10 + 1]> self = ?,<br>Tensor other = -3.3895313892515355e+38 | Unknown  | Unknown    | N/A                   | N/A    |
|  32 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.03125                       | Unknown  | Done       | 1.0                   | 0      |
|  33 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999952666163154    | 0      |
|  34 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.125                         | Unknown  | Done       | 1.0                   | 0      |
|  35 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  36 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999971857745236    | 0      |
|  37 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?               | Unknown  | Done       | 0.9999966478290963    | 0      |
|  38 | Tensor<[1, 1, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                  | Unknown  | Done       | 0.9999952429161709    | 0      |
|  39 | Tensor<[1, 1, 16, 32]> self = ?,<br>Tensor<[1, 1, 1, 32]> other = ?            | Unknown  | Done       | 0.9999968593164303    | 0      |
|  40 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.448                     | Done     | Done       | 0.9999951816139105    | 0      |
|  41 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.45                      | Done     | Done       | 0.9999956498879081    | 0      |
|  42 | Tensor<[1, 1, 224, 224]> self = ?,<br>Tensor other = 0.458                     | Done     | Done       | 0.9999965333924218    | 0      |
|  43 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999951118770039    | 0      |
|  44 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  45 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999975917501909    | 0      |
|  46 | Tensor<[1, 1, 3072]> self = ?,<br>Tensor<[1, 1, 3072]> other = ?               | Unknown  | Done       | 0.9999957452669707    | 0      |
|  47 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = -0.75                        | Done     | Done       | 0.9999971581833954    | 0      |
|  48 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor other = 1.25                         | Done     | Done       | 0.9999995874297803    | 0      |
|  49 | Tensor<[1, 1, 32, 1]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?             | Done     | Done       | 0.9999977531918064    | 0      |
|  50 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999956270000885    | 0      |
|  51 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
|  52 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.99999718728752      | 0      |
|  53 | Tensor<[1, 1, 4096]> self = ?,<br>Tensor<[1, 1, 4096]> other = ?               | Unknown  | Done       | 0.9999962797292609    | 0      |
|  54 | Tensor<[1, 1, 480, 640]> self = ?,<br>Tensor other = 10                        | Done     | Done       | 0.9999985507802415    | 0      |
|  55 | Tensor<[1, 1, 512]> self = ?,<br>Tensor other = 0.04419417382415922            | Unknown  | Done       | 0.9999954427420521    | 0      |
|  56 | Tensor<[1, 1, 512]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999968349887374    | 0      |
|  57 | Tensor<[1, 1, 768]> self = ?,<br>Tensor other = 0.03608439182435161            | Unknown  | Done       | 0.9999967546400389    | 0      |
|  58 | Tensor<[1, 1, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                   | Unknown  | Done       | 0.9999968980413133    | 0      |
|  59 | Tensor<[1, 10, 1024]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                | Unknown  | Done       | 0.9999961506837673    | 0      |
|  60 | Tensor<[1, 10, 512]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999950501214427    | 0      |
|  61 | Tensor<[1, 10, 768]> self = ?,<br>Tensor<[1, 10, 1]> other = ?                 | Unknown  | Done       | 0.9999960923966795    | 0      |
|  62 | Tensor<[1, 1024, 1, 1]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999967157975566    | 0      |
|  63 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999960470930059    | 0      |
|  64 | Tensor<[1, 1024, 45, 80]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Done     | Done       | 0.999995889016913     | 0      |
|  65 | Tensor<[1, 1024, 50, 68]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?       | Unknown  | Done       | 0.9999960843418446    | 0      |
|  66 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 1, 1]> other = ?         | Done     | Done       | 0.9999958764447047    | 0      |
|  67 | Tensor<[1, 1024, 7, 7]> self = ?,<br>Tensor<[1, 1024, 7, 7]> other = ?         | Done     | Done       | 0.9999960452925489    | 0      |
|  68 | Tensor<[1, 104, 1, 1]> self = ?,<br>Tensor<[1, 104, 28, 28]> other = ?         | Done     | Done       | 0.9999962386753174    | 0      |
|  69 | Tensor<[1, 1056, 1, 1]> self = ?,<br>Tensor<[1, 1056, 48, 48]> other = ?       | Done     | Done       | 0.999995975355987     | 0      |
|  70 | Tensor<[1, 10]> self = ?,<br>Tensor<[1, 10]> other = ?                         | Done     | Done       | 0.9999982099895216    | 0      |
|  71 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999952804382568    | 0      |
|  72 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  73 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971623581336    | 0      |
|  74 | Tensor<[1, 12, 3072]> self = ?,<br>Tensor<[1, 12, 3072]> other = ?             | Done     | Done       | 0.9999960190032819    | 0      |
|  75 | Tensor<[1, 12, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
|  76 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 14, 14]> other = ?         | Done     | Done       | 0.9999954346451373    | 0      |
|  77 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?         | Done     | Done       | 0.9999958797365474    | 0      |
|  78 | Tensor<[1, 120, 1, 1]> self = ?,<br>Tensor<[1, 120, 40, 40]> other = ?         | Unknown  | Done       | 0.9999957119619659    | 0      |
|  79 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 1, 1]> other = ?         | Done     | Done       | 0.9999958000763881    | 0      |
|  80 | Tensor<[1, 120, 28, 28]> self = ?,<br>Tensor<[1, 120, 28, 28]> other = ?       | Done     | Done       | 0.9999959527904887    | 0      |
|  81 | Tensor<[1, 1232, 1, 1]> self = ?,<br>Tensor<[1, 1232, 14, 14]> other = ?       | Done     | Done       | 0.9999959618709915    | 0      |
|  82 | Tensor<[1, 128, 1, 1]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?           | Done     | Done       | 0.9999980840588429    | 0      |
|  83 | Tensor<[1, 128, 100, 136]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | 0.9999959050948689    | 0      |
|  84 | Tensor<[1, 128, 180, 320]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Done     | Done       | 0.9999959079866753    | 0      |
|  85 | Tensor<[1, 128, 200, 272]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?       | Unknown  | Done       | 0.9999959821724913    | 0      |
|  86 | Tensor<[1, 128, 90, 160]> self = ?,<br>Tensor<[1, 128, 1, 1]> other = ?        | Done     | Done       | 0.9999959531123763    | 0      |
|  87 | Tensor<[1, 1392, 1, 1]> self = ?,<br>Tensor<[1, 1392, 14, 14]> other = ?       | Done     | Done       | 0.9999958921435157    | 0      |
|  88 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.999995515364204     | 0      |
|  89 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
|  90 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999972388607969    | 0      |
|  91 | Tensor<[1, 14, 3072]> self = ?,<br>Tensor<[1, 14, 3072]> other = ?             | Done     | Done       | 0.9999959901250008    | 0      |
|  92 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 14, 14]> other = ?         | Done     | Done       | 0.9999957493126773    | 0      |
|  93 | Tensor<[1, 144, 1, 1]> self = ?,<br>Tensor<[1, 144, 28, 28]> other = ?         | Done     | Done       | 0.9999959228379879    | 0      |
|  94 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.9999952065176633    | 0      |
|  95 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
|  96 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.9999973946118343    | 0      |
|  97 | Tensor<[1, 15, 1024]> self = ?,<br>Tensor<[1, 15, 1024]> other = ?             | Unknown  | Done       | 0.9999957226469952    | 0      |
|  98 | Tensor<[1, 15, 512]> self = ?,<br>Tensor<[1, 15, 1]> other = ?                 | Unknown  | Done       | 0.9999961126637535    | 0      |
|  99 | Tensor<[1, 1512, 1, 1]> self = ?,<br>Tensor<[1, 1512, 7, 7]> other = ?         | Done     | Done       | 0.9999958126999136    | 0      |
| 100 | Tensor<[1, 16, 1, 1]> self = ?,<br>Tensor<[1, 16, 56, 56]> other = ?           | Done     | Done       | 0.9999968772696638    | 0      |
| 101 | Tensor<[1, 16, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
| 102 | Tensor<[1, 160]> self = ?,<br>Tensor other = 1                                 | Unknown  | Done       | 1.0                   | 0      |
| 103 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999969885409187    | 0      |
| 104 | Tensor<[1, 184, 14, 14]> self = ?,<br>Tensor<[1, 184, 14, 14]> other = ?       | Done     | Done       | 0.9999959754074568    | 0      |
| 105 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 0.125                        | Done     | Done       | 1.0                   | 0      |
| 106 | Tensor<[1, 19, 1024]> self = ?,<br>Tensor other = 32.0                         | Done     | Done       | 1.0                   | 0      |
| 107 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 1, 42]> other = ?          | Done     | Done       | 0.9999963379416612    | 0      |
| 108 | Tensor<[1, 192, 32, 42]> self = ?,<br>Tensor<[1, 1, 32, 1]> other = ?          | Done     | Done       | 0.9999956126741287    | 0      |
| 109 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                | Done     | Done       | 0.9999961801839254    | 0      |
| 110 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?           | Done     | Done       | 0.9999959567482127    | 0      |
| 111 | Tensor<[1, 197, 1024]> self = ?,<br>Tensor<[1024]> other = ?                   | Done     | Done       | 0.9999961620036225    | 0      |
| 112 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999950476291796    | 0      |
| 113 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?             | Done     | Done       | 0.9999959992367962    | 0      |
| 114 | Tensor<[1, 197, 768]> self = ?,<br>Tensor<[768]> other = ?                     | Done     | Done       | 0.9999959084620117    | 0      |
| 115 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 116 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 160]> other = ?                         | Unknown  | Done       | 0.9999959439347182    | 0      |
| 117 | Tensor<[1, 1]> self = ?,<br>Tensor<[1, 512]> other = ?                         | Unknown  | Done       | 0.9999956250576699    | 0      |
| 118 | Tensor<[1, 200, 14, 14]> self = ?,<br>Tensor<[1, 200, 14, 14]> other = ?       | Done     | Done       | 0.9999959609036438    | 0      |
| 119 | Tensor<[1, 2016, 1, 1]> self = ?,<br>Tensor<[1, 2016, 7, 7]> other = ?         | Done     | Unknown    | N/A                   | N/A    |
| 120 | Tensor<[1, 2048, 1, 1]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?         | Done     | Done       | 0.9999962297852667    | 0      |
| 121 | Tensor<[1, 2048, 23, 40]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Done     | Done       | 0.999995897410258     | 0      |
| 122 | Tensor<[1, 2048, 25, 34]> self = ?,<br>Tensor<[1, 2048, 1, 1]> other = ?       | Unknown  | Done       | 0.9999959443933547    | 0      |
| 123 | Tensor<[1, 208, 1, 1]> self = ?,<br>Tensor<[1, 208, 14, 14]> other = ?         | Done     | Done       | 0.9999958348440712    | 0      |
| 124 | Tensor<[1, 216, 1, 1]> self = ?,<br>Tensor<[1, 216, 28, 28]> other = ?         | Done     | Done       | 0.999996267513465     | 0      |
| 125 | Tensor<[1, 224, 1, 1]> self = ?,<br>Tensor<[1, 224, 56, 56]> other = ?         | Done     | Done       | 0.9999962610007591    | 0      |
| 126 | Tensor<[1, 23, 40]> self = ?,<br>Tensor other = 6.283185307179586              | Done     | Done       | 0.9999959562206415    | 0      |
| 127 | Tensor<[1, 232, 1, 1]> self = ?,<br>Tensor<[1, 232, 56, 56]> other = ?         | Done     | Done       | 0.999995928638917     | 0      |
| 128 | Tensor<[1, 24, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958721914309    | 0      |
| 129 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
| 130 | Tensor<[1, 24, 64, 64]> self = ?,<br>Tensor<[24, 1, 1]> other = ?              | Done     | Done       | 0.9999961056697577    | 0      |
| 131 | Tensor<[1, 24, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | 0      |
| 132 | Tensor<[1, 240, 1, 1]> self = ?,<br>Tensor<[1, 240, 14, 14]> other = ?         | Done     | Done       | 0.9999961136252876    | 0      |
| 133 | Tensor<[1, 240, 28, 28]> self = ?,<br>Tensor<[1, 240, 28, 28]> other = ?       | Done     | Done       | 0.999996027604378     | 0      |
| 134 | Tensor<[1, 256, 1, 1]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?           | Done     | Done       | 0.9999956794130904    | 0      |
| 135 | Tensor<[1, 256, 100, 136]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.9999960066213709    | 0      |
| 136 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor other = ?                       | Done     | Unknown    | N/A                   | N/A    |
| 137 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128, 1]> other = ?             | Done     | Done       | 0.9999959254170657    | 0      |
| 138 | Tensor<[1, 256, 128, 128]> self = ?,<br>Tensor<[128]> other = ?                | Done     | Done       | 0.999996042164265     | 0      |
| 139 | Tensor<[1, 256, 180, 320]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Done     | Done       | 0.9999960203037791    | 0      |
| 140 | Tensor<[1, 256, 200, 272]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?       | Unknown  | Done       | 0.9999960868462769    | 0      |
| 141 | Tensor<[1, 256, 256]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999962544419311    | 0      |
| 142 | Tensor<[1, 256, 45, 80]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.999995907417613     | 0      |
| 143 | Tensor<[1, 256, 50, 68]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Unknown  | Done       | 0.9999959784574991    | 0      |
| 144 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?         | Done     | Done       | 0.9999958835497298    | 0      |
| 145 | Tensor<[1, 256, 56, 56]> self = ?,<br>Tensor<[1, 256, 56, 56]> other = ?       | Done     | Done       | 0.9999959111677081    | 0      |
| 146 | Tensor<[1, 256, 90, 160]> self = ?,<br>Tensor<[1, 256, 1, 1]> other = ?        | Done     | Done       | 0.9999962252884937    | 0      |
| 147 | Tensor<[1, 288, 1, 1]> self = ?,<br>Tensor<[1, 288, 7, 7]> other = ?           | Done     | Done       | 0.999995867203333     | 0      |
| 148 | Tensor<[1, 2904, 1, 1]> self = ?,<br>Tensor<[1, 2904, 24, 24]> other = ?       | Done     | Done       | 0.9999959661756751    | 0      |
| 149 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor other = ?                         | Unknown  | Unknown    | N/A                   | N/A    |
| 150 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300, 1]> other = ?               | Unknown  | Done       | 0.9999958496499707    | 0      |
| 151 | Tensor<[1, 3, 300, 300]> self = ?,<br>Tensor<[300]> other = ?                  | Unknown  | Done       | 0.9999960250121421    | 0      |
| 152 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor other = ?                         | Unknown  | Unknown    | N/A                   | N/A    |
| 153 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320, 1]> other = ?               | Unknown  | Done       | 0.9999958514254714    | 0      |
| 154 | Tensor<[1, 3, 320, 320]> self = ?,<br>Tensor<[320]> other = ?                  | Unknown  | Done       | 0.9999959979153369    | 0      |
| 155 | Tensor<[1, 3, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 156 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor other = ?                        | Unknown  | Unknown    | N/A                   | N/A    |
| 157 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[1066]> other = ?                | Unknown  | Done       | 0.9999959936719269    | 0      |
| 158 | Tensor<[1, 3, 800, 1066]> self = ?,<br>Tensor<[800, 1]> other = ?              | Unknown  | Done       | 0.9999959499620042    | 0      |
| 159 | Tensor<[1, 3024, 1, 1]> self = ?,<br>Tensor<[1, 3024, 7, 7]> other = ?         | Done     | Done       | 0.9999959735953328    | 0      |
| 160 | Tensor<[1, 32, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957768327072    | 0      |
| 161 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953691336566    | 0      |
| 162 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 163 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor other = 0.79788456                   | Done     | Done       | 0.9999972118548087    | 0      |
| 164 | Tensor<[1, 32, 6144]> self = ?,<br>Tensor<[1, 32, 6144]> other = ?             | Done     | Done       | 0.9999959377988576    | 0      |
| 165 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor other = 16                         | Done     | Done       | 1.0                   | 0      |
| 166 | Tensor<[1, 32, 64, 64]> self = ?,<br>Tensor<[32, 1, 1]> other = ?              | Done     | Done       | 0.9999954096964158    | 0      |
| 167 | Tensor<[1, 320, 1, 1]> self = ?,<br>Tensor<[1, 320, 14, 14]> other = ?         | Done     | Done       | 0.999995708115643     | 0      |
| 168 | Tensor<[1, 32]> self = ?,<br>Tensor<[1, 32]> other = ?                         | Done     | Done       | 0.9999954048722932    | 0      |
| 169 | Tensor<[1, 336, 1, 1]> self = ?,<br>Tensor<[1, 336, 14, 14]> other = ?         | Done     | Done       | 0.9999959306735787    | 0      |
| 170 | Tensor<[1, 3712, 1, 1]> self = ?,<br>Tensor<[1, 3712, 7, 7]> other = ?         | Done     | Done       | 0.999995982877641     | 0      |
| 171 | Tensor<[1, 4, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 172 | Tensor<[1, 4096, 1280]> self = ?,<br>Tensor<[1, 4096, 1280]> other = ?         | Unknown  | Done       | 0.9999959557523591    | 0      |
| 173 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor<[1, 1, 1]> other = ?                 | Done     | Done       | 0.9999966249434357    | 0      |
| 174 | Tensor<[1, 440, 1, 1]> self = ?,<br>Tensor<[1, 440, 7, 7]> other = ?           | Done     | Done       | 0.9999959228430797    | 0      |
| 175 | Tensor<[1, 448, 1, 1]> self = ?,<br>Tensor<[1, 448, 28, 28]> other = ?         | Done     | Done       | 0.9999959458827716    | 0      |
| 176 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.044715                     | Unknown  | Done       | 0.99999541929097      | 0      |
| 177 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.5                          | Unknown  | Done       | 1.0                   | 0      |
| 178 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor other = 0.7978845608028654           | Unknown  | Done       | 0.999997187261139     | 0      |
| 179 | Tensor<[1, 45, 3072]> self = ?,<br>Tensor<[1, 45, 3072]> other = ?             | Unknown  | Done       | 0.9999960161275622    | 0      |
| 180 | Tensor<[1, 48, 1, 1]> self = ?,<br>Tensor<[1, 48, 56, 56]> other = ?           | Done     | Done       | 0.999996582420918     | 0      |
| 181 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 10, 10]> other = ?         | Unknown  | Done       | 0.9999961590950545    | 0      |
| 182 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?         | Done     | Done       | 0.9999960554987884    | 0      |
| 183 | Tensor<[1, 480, 1, 1]> self = ?,<br>Tensor<[1, 480, 20, 20]> other = ?         | Unknown  | Done       | 0.9999959845345281    | 0      |
| 184 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 1, 1]> other = ?         | Done     | Done       | 0.9999960060696368    | 0      |
| 185 | Tensor<[1, 480, 14, 14]> self = ?,<br>Tensor<[1, 480, 14, 14]> other = ?       | Done     | Done       | 0.9999959557485986    | 0      |
| 186 | Tensor<[1, 5, 16, 32]> self = ?,<br>Tensor<[1, 5, 1, 32]> other = ?            | Unknown  | Done       | 0.9999949883361404    | 0      |
| 187 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.044715                      | Unknown  | Done       | 0.9999953456059629    | 0      |
| 188 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.5                           | Unknown  | Done       | 1.0                   | 0      |
| 189 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Unknown  | Done       | 0.9999973175588065    | 0      |
| 190 | Tensor<[1, 5, 4096]> self = ?,<br>Tensor<[1, 5, 4096]> other = ?               | Unknown  | Done       | 0.9999958744427324    | 0      |
| 191 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor other = 1.702                        | Done     | Done       | 0.9999960045978077    | 0      |
| 192 | Tensor<[1, 50, 3072]> self = ?,<br>Tensor<[1, 50, 3072]> other = ?             | Done     | Done       | 0.9999959499183169    | 0      |
| 193 | Tensor<[1, 50, 768]> self = ?,<br>Tensor other = 0.125                         | Done     | Done       | 1.0                   | 0      |
| 194 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?           | Done     | Done       | 0.9999952426241664    | 0      |
| 195 | Tensor<[1, 512, 1, 1]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ?         | Unknown  | Done       | 0.9999960793933642    | 0      |
| 196 | Tensor<[1, 512, 100, 136]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?       | Unknown  | Done       | 0.9999957858927674    | 0      |
| 197 | Tensor<[1, 512, 23, 40]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999956656635945    | 0      |
| 198 | Tensor<[1, 512, 25, 34]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | 0.9999960933917068    | 0      |
| 199 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999958774315729    | 0      |
| 200 | Tensor<[1, 512, 28, 28]> self = ?,<br>Tensor<[1, 512, 28, 28]> other = ?       | Done     | Done       | 0.9999959172595514    | 0      |
| 201 | Tensor<[1, 512, 45, 80]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Done     | Done       | 0.9999958431699724    | 0      |
| 202 | Tensor<[1, 512, 50, 68]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?         | Unknown  | Done       | 0.99999612014397      | 0      |
| 203 | Tensor<[1, 512, 90, 160]> self = ?,<br>Tensor<[1, 512, 1, 1]> other = ?        | Done     | Done       | 0.9999959648867193    | 0      |
| 204 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                       | Unknown  | Done       | 0.9999961576058889    | 0      |
| 205 | Tensor<[1, 528, 1, 1]> self = ?,<br>Tensor<[1, 528, 96, 96]> other = ?         | Done     | Done       | 0.9999959597619911    | 0      |
| 206 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 14, 14]> other = ?         | Done     | Done       | 0.9999959115784366    | 0      |
| 207 | Tensor<[1, 576, 1, 1]> self = ?,<br>Tensor<[1, 576, 7, 7]> other = ?           | Done     | Done       | 0.9999958912961209    | 0      |
| 208 | Tensor<[1, 59, 1024]> self = ?,<br>Tensor other = 0.125                        | Unknown  | Done       | 1.0                   | 0      |
| 209 | Tensor<[1, 59]> self = ?,<br>Tensor<[1, 59]> other = ?                         | Unknown  | Done       | 0.999997250317147     | 0      |
| 210 | Tensor<[1, 6, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 211 | Tensor<[1, 60]> self = ?,<br>Tensor<[1, 60]> other = ?                         | Unknown  | Done       | 0.9999949094923838    | 0      |
| 212 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?             | Done     | Done       | 0.9999976204974027    | 0      |
| 213 | Tensor<[1, 64, 1, 1]> self = ?,<br>Tensor<[1, 64, 56, 56]> other = ?           | Done     | Done       | 0.9999956957014313    | 0      |
| 214 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 215 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[1, 1, 120, 160]> other = ?      | Done     | Done       | 0.9999959120798135    | 0      |
| 216 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[120, 1]> other = ?              | Done     | Done       | 0.9999960273197034    | 0      |
| 217 | Tensor<[1, 64, 120, 160]> self = ?,<br>Tensor<[160]> other = ?                 | Done     | Done       | 0.9999958208082135    | 0      |
| 218 | Tensor<[1, 64, 180, 320]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999955605865999    | 0      |
| 219 | Tensor<[1, 64, 200, 272]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | 0.9999955846472579    | 0      |
| 220 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 221 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[240, 1]> other = ?              | Done     | Done       | 0.999995997321473     | 0      |
| 222 | Tensor<[1, 64, 240, 320]> self = ?,<br>Tensor<[320]> other = ?                 | Done     | Done       | 0.999995684879551     | 0      |
| 223 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 224 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[1, 1, 30, 40]> other = ?          | Done     | Done       | 0.9999959446653807    | 0      |
| 225 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[30, 1]> other = ?                 | Done     | Done       | 0.9999953452475154    | 0      |
| 226 | Tensor<[1, 64, 30, 40]> self = ?,<br>Tensor<[40]> other = ?                    | Done     | Done       | 0.9999965892056233    | 0      |
| 227 | Tensor<[1, 64, 360, 640]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Done     | Done       | 0.9999957422525227    | 0      |
| 228 | Tensor<[1, 64, 400, 544]> self = ?,<br>Tensor<[1, 64, 1, 1]> other = ?         | Unknown  | Done       | 0.9999958568411058    | 0      |
| 229 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor other = ?                        | Done     | Unknown    | N/A                   | N/A    |
| 230 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[480, 1]> other = ?              | Done     | Done       | 0.9999960507662341    | 0      |
| 231 | Tensor<[1, 64, 480, 640]> self = ?,<br>Tensor<[640]> other = ?                 | Done     | Done       | 0.9999958139089536    | 0      |
| 232 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor other = ?                          | Done     | Unknown    | N/A                   | N/A    |
| 233 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[1, 1, 60, 80]> other = ?          | Done     | Done       | 0.9999959534746011    | 0      |
| 234 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[60, 1]> other = ?                 | Done     | Done       | 0.9999960425391443    | 0      |
| 235 | Tensor<[1, 64, 60, 80]> self = ?,<br>Tensor<[80]> other = ?                    | Done     | Done       | 0.9999962286147313    | 0      |
| 236 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 10, 10]> other = ?         | Unknown  | Done       | 0.9999958938499198    | 0      |
| 237 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?         | Done     | Done       | 0.9999960640595298    | 0      |
| 238 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 20, 20]> other = ?         | Unknown  | Done       | 0.9999960073521945    | 0      |
| 239 | Tensor<[1, 672, 1, 1]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999957806890883    | 0      |
| 240 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?         | Done     | Done       | 0.9999958921967356    | 0      |
| 241 | Tensor<[1, 672, 14, 14]> self = ?,<br>Tensor<[1, 672, 14, 14]> other = ?       | Done     | Done       | 0.9999959335336132    | 0      |
| 242 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 1, 1]> other = ?           | Done     | Done       | 0.9999960380223385    | 0      |
| 243 | Tensor<[1, 672, 7, 7]> self = ?,<br>Tensor<[1, 672, 7, 7]> other = ?           | Done     | Done       | 0.9999959361780866    | 0      |
| 244 | Tensor<[1, 696, 1, 1]> self = ?,<br>Tensor<[1, 696, 28, 28]> other = ?         | Done     | Done       | 0.9999958722149039    | 0      |
| 245 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953528388896    | 0      |
| 246 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 247 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999971638436844    | 0      |
| 248 | Tensor<[1, 7, 3072]> self = ?,<br>Tensor<[1, 7, 3072]> other = ?               | Done     | Done       | 0.9999957953038436    | 0      |
| 249 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?           | Done     | Done       | 0.9999950109490965    | 0      |
| 250 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 40, 40]> other = ?           | Unknown  | Done       | 0.999996571601195     | 0      |
| 251 | Tensor<[1, 72, 1, 1]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?           | Done     | Done       | 0.9999962613883483    | 0      |
| 252 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 1, 1]> other = ?           | Done     | Done       | 0.9999958719162162    | 0      |
| 253 | Tensor<[1, 72, 28, 28]> self = ?,<br>Tensor<[1, 72, 28, 28]> other = ?         | Done     | Done       | 0.9999959779622053    | 0      |
| 254 | Tensor<[1, 72, 56, 56]> self = ?,<br>Tensor<[1, 72, 56, 56]> other = ?         | Done     | Done       | 0.9999959015340175    | 0      |
| 255 | Tensor<[1, 7392, 1, 1]> self = ?,<br>Tensor<[1, 7392, 12, 12]> other = ?       | Done     | Done       | 0.9999959122049976    | 0      |
| 256 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 1, 1]> other = ?         | Done     | Done       | 0.9999960174239634    | 0      |
| 257 | Tensor<[1, 768, 14, 14]> self = ?,<br>Tensor<[1, 768, 14, 14]> other = ?       | Done     | Done       | 0.9999960097805805    | 0      |
| 258 | Tensor<[1, 784, 1, 1]> self = ?,<br>Tensor<[1, 784, 7, 7]> other = ?           | Done     | Done       | 0.9999957670709981    | 0      |
| 259 | Tensor<[1, 8, 64, 64]> self = ?,<br>Tensor other = 16                          | Done     | Done       | 1.0                   | 0      |
| 260 | Tensor<[1, 888, 1, 1]> self = ?,<br>Tensor<[1, 888, 7, 7]> other = ?           | Done     | Done       | 0.9999960304589269    | 0      |
| 261 | Tensor<[1, 896, 1, 1]> self = ?,<br>Tensor<[1, 896, 14, 14]> other = ?         | Done     | Unknown    | N/A                   | N/A    |
| 262 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.044715                       | Done     | Done       | 0.9999952420227186    | 0      |
| 263 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.5                            | Done     | Done       | 1.0                   | 0      |
| 264 | Tensor<[1, 9, 128]> self = ?,<br>Tensor other = 0.7978845608028654             | Done     | Done       | 0.9999972078151116    | 0      |
| 265 | Tensor<[1, 9, 128]> self = ?,<br>Tensor<[1, 9, 128]> other = ?                 | Done     | Done       | 0.9999959529878216    | 0      |
| 266 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.044715                     | Done     | Done       | 0.9999953772759759    | 0      |
| 267 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.5                          | Done     | Done       | 1.0                   | 0      |
| 268 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor other = 0.7978845608028654           | Done     | Done       | 0.9999971981424188    | 0      |
| 269 | Tensor<[1, 9, 16384]> self = ?,<br>Tensor<[1, 9, 16384]> other = ?             | Done     | Done       | 0.9999959159149057    | 0      |
| 270 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953815143361    | 0      |
| 271 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 272 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972050502816    | 0      |
| 273 | Tensor<[1, 9, 3072]> self = ?,<br>Tensor<[1, 9, 3072]> other = ?               | Done     | Done       | 0.9999956622483802    | 0      |
| 274 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999954053000204    | 0      |
| 275 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 276 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972906987658    | 0      |
| 277 | Tensor<[1, 9, 4096]> self = ?,<br>Tensor<[1, 9, 4096]> other = ?               | Done     | Done       | 0.9999959922956179    | 0      |
| 278 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.044715                      | Done     | Done       | 0.9999953774343205    | 0      |
| 279 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.5                           | Done     | Done       | 1.0                   | 0      |
| 280 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor other = 0.7978845608028654            | Done     | Done       | 0.9999972114302971    | 0      |
| 281 | Tensor<[1, 9, 8192]> self = ?,<br>Tensor<[1, 9, 8192]> other = ?               | Done     | Done       | 0.9999960773554755    | 0      |
| 282 | Tensor<[1, 96, 1, 1]> self = ?,<br>Tensor<[1, 96, 14, 14]> other = ?           | Done     | Done       | 0.9999955311721199    | 0      |
| 283 | Tensor<[1, 960, 1, 1]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999958390727209    | 0      |
| 284 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 1, 1]> other = ?           | Done     | Done       | 0.999996091487582     | 0      |
| 285 | Tensor<[1, 960, 7, 7]> self = ?,<br>Tensor<[1, 960, 7, 7]> other = ?           | Done     | Done       | 0.9999958300823408    | 0      |
| 286 | Tensor<[1, s0*s1, 2560]> self = ?,<br>Tensor<[1, s0*s1, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 287 | Tensor<[1, s0*s1, 5120]> self = ?,<br>Tensor<[1, s0*s1, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 288 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor<[1, s1*s2, 1280]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 289 | Tensor<[1, s1*s2, 2560]> self = ?,<br>Tensor<[1, s1*s2, 2560]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 290 | Tensor<[1, s1*s2, 5120]> self = ?,<br>Tensor<[1, s1*s2, 5120]> other = ?       | Unknown  | Unknown    | N/A                   | N/A    |
| 291 | Tensor<[1, s10 + 1]> self = ?,<br>Tensor<[1, s10 + 1]> other = ?               | Unknown  | Unknown    | N/A                   | N/A    |
| 292 | Tensor<[10, 10]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 293 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 294 | Tensor<[1024]> self = ?,<br>Tensor<[1, 1, 1024]> other = ?                     | Unknown  | Done       | 0.9999961395507391    | 0      |
| 295 | Tensor<[1024]> self = ?,<br>Tensor<[1, 10, 1024]> other = ?                    | Unknown  | Done       | 0.9999961798436685    | 0      |
| 296 | Tensor<[1024]> self = ?,<br>Tensor<[1, 197, 1024]> other = ?                   | Done     | Done       | 0.9999958184906064    | 0      |
| 297 | Tensor<[128]> self = ?,<br>Tensor other = 2                                    | Done     | Done       | 1.0                   | 0      |
| 298 | Tensor<[12]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 299 | Tensor<[15, 15]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 300 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                                 | Unknown  | Done       | 1.0                   | 0      |
| 301 | Tensor<[16, 6, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958029767626    | 0      |
| 302 | Tensor<[16, 6, 64, 64]> self = ?,<br>Tensor<[6, 1, 1]> other = ?               | Done     | Done       | -0.011784401587547965 | 0      |
| 303 | Tensor<[16, 8, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999957964321247    | 0      |
| 304 | Tensor<[16, 8, 64, 64]> self = ?,<br>Tensor<[8, 1, 1]> other = ?               | Done     | Done       | 0.024461238003952137  | 0      |
| 305 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                                | Unknown  | Done       | 1.0                   | 0      |
| 306 | Tensor<[2*s0]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 307 | Tensor<[2*s1]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 308 | Tensor<[2*s2]> self = ?,<br>Tensor<0.500000000000000> other = ?                | Unknown  | Unknown    | N/A                   | N/A    |
| 309 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 1]> other = ?                           | Unknown  | Done       | 1.0                   | 0      |
| 310 | Tensor<[2, 1]> self = ?,<br>Tensor<[2, 512]> other = ?                         | Unknown  | Done       | 0.9999956812205112    | 0      |
| 311 | Tensor<[2, 1]> self = ?,<br>Tensor<[]> other = ?                               | None     | Fallback   | 1.0                   | -1     |
| 312 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                                  | Unknown  | Done       | 1.0                   | 0      |
| 313 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 512]> other = ?                       | Unknown  | Done       | 0.9999959456419942    | 0      |
| 314 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor other = 1.702                         | Done     | Done       | 0.9999960038127856    | 0      |
| 315 | Tensor<[2, 7, 2048]> self = ?,<br>Tensor<[2, 7, 2048]> other = ?               | Done     | Done       | 0.9999960931542436    | 0      |
| 316 | Tensor<[2, 7, 512]> self = ?,<br>Tensor other = 0.125                          | Done     | Done       | 1.0                   | 0      |
| 317 | Tensor<[25]> self = ?,<br>Tensor<[]> other = ?                                 | Unknown  | Fallback   | 1.0                   | -1     |
| 318 | Tensor<[300]> self = ?,<br>Tensor<[]> other = ?                                | Unknown  | Fallback   | 1.0                   | -1     |
| 319 | Tensor<[3234, 1]> self = ?,<br>Tensor<[3234, 1]> other = ?                     | Unknown  | Done       | 0.9999963574110621    | 0      |
| 320 | Tensor<[3234, 2]> self = ?,<br>Tensor other = 0.5                              | Unknown  | Done       | 1.0                   | 0      |
| 321 | Tensor<[3234, 2]> self = ?,<br>Tensor other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
| 322 | Tensor<[3234]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Done       | 1.0                   | 0      |
| 323 | Tensor<[4, 12, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999959174750042    | 0      |
| 324 | Tensor<[4, 12, 64, 64]> self = ?,<br>Tensor<[12, 1, 1]> other = ?              | Done     | Done       | 0.2312208894437325    | 0      |
| 325 | Tensor<[4, 16, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958538468114    | 0      |
| 326 | Tensor<[4, 16, 64, 64]> self = ?,<br>Tensor<[16, 1, 1]> other = ?              | Done     | Done       | 0.2662866736510318    | 0      |
| 327 | Tensor<[512]> self = ?,<br>Tensor<[1, 1, 512]> other = ?                       | Unknown  | Done       | 0.9999961544905543    | 0      |
| 328 | Tensor<[512]> self = ?,<br>Tensor<[1, 10, 512]> other = ?                      | Unknown  | Done       | 0.9999954448803435    | 0      |
| 329 | Tensor<[512]> self = ?,<br>Tensor<[1, 15, 512]> other = ?                      | Unknown  | Done       | 0.9999958615466823    | 0      |
| 330 | Tensor<[64, 3, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958478615228    | 0      |
| 331 | Tensor<[64, 3, 64, 64]> self = ?,<br>Tensor<[3, 1, 1]> other = ?               | Done     | Done       | 0.06620762809467126   | 0      |
| 332 | Tensor<[64, 4, 49, 32]> self = ?,<br>Tensor other = 0.1767766952966369         | Done     | Done       | 0.9999958343232078    | 0      |
| 333 | Tensor<[64, 4, 64, 64]> self = ?,<br>Tensor<[4, 1, 1]> other = ?               | Done     | Done       | -0.03455422025971569  | 0      |
| 334 | Tensor<[768]> self = ?,<br>Tensor<[1, 1, 768]> other = ?                       | Unknown  | Done       | 0.9999967018852842    | 0      |
| 335 | Tensor<[768]> self = ?,<br>Tensor<[1, 10, 768]> other = ?                      | Unknown  | Done       | 0.9999958657699086    | 0      |
| 336 | Tensor<[768]> self = ?,<br>Tensor<[1, 197, 768]> other = ?                     | Done     | Done       | 0.9999961338831972    | 0      |
| 337 | Tensor<[8732, 1]> self = ?,<br>Tensor<[8732, 1]> other = ?                     | Unknown  | Done       | 0.9999956661774084    | 0      |
| 338 | Tensor<[8732, 2]> self = ?,<br>Tensor other = 0.5                              | Unknown  | Done       | 1.0                   | 0      |
| 339 | Tensor<[8732, 2]> self = ?,<br>Tensor other = ?                                | Unknown  | Unknown    | N/A                   | N/A    |
| 340 | Tensor<[8732]> self = ?,<br>Tensor other = 0.5                                 | Unknown  | Done       | 1.0                   | 0      |
| 341 | Tensor<[]> self = ?,<br>Tensor<[1, 24, 768]> other = ?                         | None     | Fallback   | 1.0                   | -1     |
| 342 | Tensor<[]> self = ?,<br>Tensor<[]> other = ?                                   | Unknown  | Fallback   | 1.0                   | -1     |
| 343 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                        | Unknown  | Unknown    | N/A                   | N/A    |

