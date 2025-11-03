### aten.div.Tensor
|     | ATen Input Variations                                                    | Status   | Isolated   | PCC                | Host   |
|----:|:-------------------------------------------------------------------------|:---------|:-----------|:-------------------|:-------|
|   0 | Tensor self = ?,<br>Tensor other = 1                                     | Done     | Unknown    | N/A                | N/A    |
|   1 | Tensor self = ?,<br>Tensor other = 1.0                                   | Done     | Unknown    | N/A                | N/A    |
|   2 | Tensor self = ?,<br>Tensor other = 10                                    | Done     | Unknown    | N/A                | N/A    |
|   3 | Tensor self = ?,<br>Tensor other = 128                                   | Done     | Unknown    | N/A                | N/A    |
|   4 | Tensor self = ?,<br>Tensor other = 160                                   | Unknown  | Unknown    | N/A                | N/A    |
|   5 | Tensor self = ?,<br>Tensor other = 18.75                                 | Done     | Unknown    | N/A                | N/A    |
|   6 | Tensor self = ?,<br>Tensor other = 2                                     | Done     | Unknown    | N/A                | N/A    |
|   7 | Tensor self = ?,<br>Tensor other = 20                                    | Done     | Unknown    | N/A                | N/A    |
|   8 | Tensor self = ?,<br>Tensor other = 3                                     | Done     | Unknown    | N/A                | N/A    |
|   9 | Tensor self = ?,<br>Tensor other = 3.0                                   | Done     | Unknown    | N/A                | N/A    |
|  10 | Tensor self = ?,<br>Tensor other = 37.5                                  | Done     | Unknown    | N/A                | N/A    |
|  11 | Tensor self = ?,<br>Tensor other = 4.6875                                | Done     | Unknown    | N/A                | N/A    |
|  12 | Tensor self = ?,<br>Tensor other = 5                                     | Done     | Unknown    | N/A                | N/A    |
|  13 | Tensor self = ?,<br>Tensor other = 9.375                                 | Done     | Unknown    | N/A                | N/A    |
|  14 | Tensor self = ?,<br>Tensor other = ?                                     | Done     | Unknown    | N/A                | N/A    |
|  15 | Tensor<[1, 1, 16384, 256]> self = ?,<br>Tensor other = 5.656854249492381 | Done     | Done       | 0.9999958415616007 | 0      |
|  16 | Tensor<[1, 1, 19200, 300]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                | 0      |
|  17 | Tensor<[1, 1, 256]> self = ?,<br>Tensor other = 0.5                      | Unknown  | Unknown    | N/A                | N/A    |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9285714253783226    | Done     | Done       | 0.9999958921963388 | 0      |
|  19 | Tensor<[1, 1024, 160]> self = ?,<br>Tensor other = 0.9428571425378323    | Done     | Done       | 0.9999962516219401 | 0      |
|  20 | Tensor<[1, 12, 10, 10]> self = ?,<br>Tensor other = 8.0                  | Removed  | Done       | 1.0                | 0      |
|  21 | Tensor<[1, 12, 12, 12]> self = ?,<br>Tensor other = 8.0                  | Removed  | Done       | 1.0                | 0      |
|  22 | Tensor<[1, 12, 14, 14]> self = ?,<br>Tensor other = 8.0                  | Removed  | Done       | 1.0                | 0      |
|  23 | Tensor<[1, 12, 16, 64]> self = ?,<br>Tensor other = 8.0                  | Done     | Done       | 1.0                | 0      |
|  24 | Tensor<[1, 12, 197, 197]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  25 | Tensor<[1, 12, 201, 201]> self = ?,<br>Tensor other = 8.0                | Unknown  | Unknown    | N/A                | N/A    |
|  26 | Tensor<[1, 12, 25, 25]> self = ?,<br>Tensor other = 8.0                  | Removed  | Done       | 1.0                | 0      |
|  27 | Tensor<[1, 12, 257, 257]> self = ?,<br>Tensor other = 8.0                | Done     | Unknown    | N/A                | N/A    |
|  28 | Tensor<[1, 12, 7, 7]> self = ?,<br>Tensor<[]> other = ?                  | Done     | Done       | 0.999995934427356  | 0      |
|  29 | Tensor<[1, 12, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Removed  | Done       | 1.0                | 0      |
|  30 | Tensor<[1, 128, 1536]> self = ?,<br>Tensor other = 3                     | Unknown  | Unknown    | N/A                | N/A    |
|  31 | Tensor<[1, 1280, 8, 8]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Done       | 1.0                | 0      |
|  32 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1                  | Unknown  | Unknown    | N/A                | N/A    |
|  33 | Tensor<[1, 1280, s0, s1]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                | N/A    |
|  34 | Tensor<[1, 1280, s1, s2]> self = ?,<br>Tensor other = 1.0                | Unknown  | Unknown    | N/A                | N/A    |
|  35 | Tensor<[1, 16, 1, 6]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999961822090166 | 0      |
|  36 | Tensor<[1, 16, 1, s10 + 1]> self = ?,<br>Tensor<[]> other = ?            | Unknown  | Unknown    | N/A                | N/A    |
|  37 | Tensor<[1, 16, 5, 5]> self = ?,<br>Tensor<[]> other = ?                  | Unknown  | Done       | 0.9999961036954848 | 0      |
|  38 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 11.313708498984761     | Removed  | Done       | 0.9999960790902892 | 0      |
|  39 | Tensor<[1, 16, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Removed  | Done       | 1.0                | 0      |
|  40 | Tensor<[1, 16384, 32]> self = ?,<br>Tensor other = 0.9857142856344581    | Done     | Done       | 0.9999979583299631 | 0      |
|  41 | Tensor<[1, 1]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                | 0      |
|  42 | Tensor<[1, 1]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                | 0      |
|  43 | Tensor<[1, 2, 4096, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958511472916 | 0      |
|  44 | Tensor<[1, 2, 4800, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  45 | Tensor<[1, 23, 40, 1]> self = ?,<br>Tensor<[128]> other = ?              | Done     | Done       | 0.9999933238755897 | 0      |
|  46 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 1, 40]> other = ?            | Done     | Unknown    | N/A                | N/A    |
|  47 | Tensor<[1, 23, 40]> self = ?,<br>Tensor<[1, 23, 1]> other = ?            | Done     | Unknown    | N/A                | N/A    |
|  48 | Tensor<[1, 24, 64, 32]> self = ?,<br>Tensor<[1, 24, 64, 32]> other = ?   | Done     | Done       | 0.9999876689874467 | 0      |
|  49 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.8999999985098839     | Done     | Done       | 0.9999965128625784 | 0      |
|  50 | Tensor<[1, 256, 256]> self = ?,<br>Tensor other = 0.9142857119441032     | Done     | Done       | 0.9999962151548265 | 0      |
|  51 | Tensor<[1, 256, 384]> self = ?,<br>Tensor other = 3                      | Unknown  | Unknown    | N/A                | N/A    |
|  52 | Tensor<[1, 3, 1445, 1445]> self = ?,<br>Tensor other = 8.0               | Done     | Done       | 1.0                | 0      |
|  53 | Tensor<[1, 32, 24576]> self = ?,<br>Tensor other = 3                     | Unknown  | Unknown    | N/A                | N/A    |
|  54 | Tensor<[1, 32, 64, 32]> self = ?,<br>Tensor<[1, 32, 64, 32]> other = ?   | Done     | Done       | 0.9999978925786326 | 0      |
|  55 | Tensor<[1, 320, 64, 64]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Done       | 1.0                | 0      |
|  56 | Tensor<[1, 320, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  57 | Tensor<[1, 4096, 320]> self = ?,<br>Tensor other = 1.0                   | Unknown  | Done       | 1.0                | 0      |
|  58 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9571428559720516     | Done     | Done       | 0.9999966978858859 | 0      |
|  59 | Tensor<[1, 4096, 64]> self = ?,<br>Tensor other = 0.9714285712689161     | Done     | Done       | 0.9999972613132535 | 0      |
|  60 | Tensor<[1, 5, 1024, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958436604448 | 0      |
|  61 | Tensor<[1, 5, 1200, 300]> self = ?,<br>Tensor other = 8.0                | Done     | Done       | 1.0                | 0      |
|  62 | Tensor<[1, 50257]> self = ?,<br>Tensor other = 0.9                       | Unknown  | Done       | 0.9999964959182386 | 0      |
|  63 | Tensor<[1, 512, 38, 38]> self = ?,<br>Tensor<[1, 512, 38, 38]> other = ? | Done     | Done       | 0.9999998186858341 | 0      |
|  64 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 1]> other = ?                   | Done     | Done       | 0.9999957596642836 | 0      |
|  65 | Tensor<[1, 512]> self = ?,<br>Tensor<[1, 512]> other = ?                 | Unknown  | Unknown    | N/A                | N/A    |
|  66 | Tensor<[1, 64, 6144]> self = ?,<br>Tensor other = 3                      | Unknown  | Unknown    | N/A                | N/A    |
|  67 | Tensor<[1, 64, 9, 9]> self = ?,<br>Tensor other = 8.0                    | Removed  | Done       | 1.0                | 0      |
|  68 | Tensor<[1, 640, s0, s1]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  69 | Tensor<[1, 640, s1, s2]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  70 | Tensor<[1, 8, 2048, 256]> self = ?,<br>Tensor other = 5.656854249492381  | Done     | Done       | 0.9999958321125948 | 0      |
|  71 | Tensor<[1, 8, 256, 2048]> self = ?,<br>Tensor other = 5.656854249492381  | Removed  | Done       | 0.9999958392082965 | 0      |
|  72 | Tensor<[1, 8, 256, 256]> self = ?,<br>Tensor other = 5.656854249492381   | Done     | Done       | 0.9999958463202513 | 0      |
|  73 | Tensor<[1, 8, 300, 300]> self = ?,<br>Tensor other = 8.0                 | Done     | Done       | 1.0                | 0      |
|  74 | Tensor<[1, s0*s1, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  75 | Tensor<[1, s0*s1, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  76 | Tensor<[1, s0, 256]> self = ?,<br>Tensor other = 0.5                     | Unknown  | Unknown    | N/A                | N/A    |
|  77 | Tensor<[1, s1*s2, 1280]> self = ?,<br>Tensor other = 1.0                 | Unknown  | Unknown    | N/A                | N/A    |
|  78 | Tensor<[1, s1*s2, 320]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  79 | Tensor<[1, s1*s2, 640]> self = ?,<br>Tensor other = 1.0                  | Unknown  | Unknown    | N/A                | N/A    |
|  80 | Tensor<[10, 10]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999957003189243 | 0      |
|  81 | Tensor<[10, 10]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                | 0      |
|  82 | Tensor<[15, 15]> self = ?,<br>Tensor other = 2.772588722239781           | Unknown  | Done       | 0.9999956361718246 | 0      |
|  83 | Tensor<[15, 15]> self = ?,<br>Tensor other = 8                           | Unknown  | Done       | 1.0                | 0      |
|  84 | Tensor<[16, 6, 64, 32]> self = ?,<br>Tensor<[16, 6, 64, 32]> other = ?   | Done     | Done       | 0.9999967899106137 | 0      |
|  85 | Tensor<[16, 8, 64, 32]> self = ?,<br>Tensor<[16, 8, 64, 32]> other = ?   | Done     | Done       | 0.99999938972147   | 0      |
|  86 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 1]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  87 | Tensor<[16384, 4]> self = ?,<br>Tensor<[16384, 4]> other = ?             | Done     | Unknown    | N/A                | N/A    |
|  88 | Tensor<[16384]> self = ?,<br>Tensor<[16384]> other = ?                   | Done     | Unknown    | N/A                | N/A    |
|  89 | Tensor<[17, 17]> self = ?,<br>Tensor other = 16                          | Unknown  | Done       | 1.0                | 0      |
|  90 | Tensor<[17, 17]> self = ?,<br>Tensor other = 2.0794415416798357          | Unknown  | Done       | 0.9999987917573541 | 0      |
|  91 | Tensor<[2, 2]> self = ?,<br>Tensor other = 16                            | Unknown  | Done       | 1.0                | 0      |
|  92 | Tensor<[2, 2]> self = ?,<br>Tensor other = 2.0794415416798357            | Unknown  | Done       | 1.0                | 0      |
|  93 | Tensor<[2, 512]> self = ?,<br>Tensor<[2, 1]> other = ?                   | Done     | Done       | 0.9999950667646001 | 0      |
|  94 | Tensor<[3, 320, 320]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999965496385548 | 0      |
|  95 | Tensor<[3, 480, 640]> self = ?,<br>Tensor<[3, 1, 1]> other = ?           | Done     | Done       | 0.9999953575888275 | 0      |
|  96 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 10.0                       | Done     | Unknown    | N/A                | N/A    |
|  97 | Tensor<[3234, 1]> self = ?,<br>Tensor other = 5.0                        | Done     | Unknown    | N/A                | N/A    |
|  98 | Tensor<[4, 12, 64, 32]> self = ?,<br>Tensor<[4, 12, 64, 32]> other = ?   | Done     | Done       | 0.9999958447294648 | 0      |
|  99 | Tensor<[4, 16, 64, 32]> self = ?,<br>Tensor<[4, 16, 64, 32]> other = ?   | Done     | Done       | 0.9999999723273505 | 0      |
| 100 | Tensor<[64, 3, 64, 32]> self = ?,<br>Tensor<[64, 3, 64, 32]> other = ?   | Done     | Done       | 0.9999959463264633 | 0      |
| 101 | Tensor<[64, 4, 64, 32]> self = ?,<br>Tensor<[64, 4, 64, 32]> other = ?   | Done     | Done       | 0.9999991695111519 | 0      |
| 102 | Tensor<[8, 100, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999957399957516 | 0      |
| 103 | Tensor<[8, 16, 384, 384]> self = ?,<br>Tensor other = 8.0                | Removed  | Unknown    | N/A                | N/A    |
| 104 | Tensor<[8, 920, 32]> self = ?,<br>Tensor other = 5.656854249492381       | Done     | Done       | 0.9999958619608199 | 0      |
| 105 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 10.0                       | Done     | Unknown    | N/A                | N/A    |
| 106 | Tensor<[8732, 1]> self = ?,<br>Tensor other = 5.0                        | Done     | Unknown    | N/A                | N/A    |
| 107 | Tensor<[96, 80]> self = ?,<br>Tensor<[80]> other = ?                     | Unknown  | Unknown    | N/A                | N/A    |
| 108 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 16                  | Unknown  | Unknown    | N/A                | N/A    |
| 109 | Tensor<[s0 + 1, s0 + 1]> self = ?,<br>Tensor other = 2.0794415416798357  | Unknown  | Unknown    | N/A                | N/A    |

