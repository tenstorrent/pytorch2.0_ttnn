### aten.transpose.int
|     | ATen Input Variations                                                     | Status   | Single-native-run   | Single-run   | Single-accuracy   | Single-converted   |
|----:|:--------------------------------------------------------------------------|:---------|:--------------------|:-------------|:------------------|:-------------------|
|   0 | Tensor<[1, 1, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|   1 | Tensor<[1, 1, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   2 | Tensor<[1, 1, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   3 | Tensor<[1, 1, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|   4 | Tensor<[1, 1, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   5 | Tensor<[1, 1, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   6 | Tensor<[1, 1, 7, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   7 | Tensor<[1, 1, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|   8 | Tensor<[1, 10, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|   9 | Tensor<[1, 10, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  10 | Tensor<[1, 10, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  11 | Tensor<[1, 1024, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  12 | Tensor<[1, 1024, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  13 | Tensor<[1, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  14 | Tensor<[1, 1024, 640]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  15 | Tensor<[1, 1024, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  16 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  17 | Tensor<[1, 12, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  18 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  19 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  20 | Tensor<[1, 12, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  21 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  22 | Tensor<[1, 12, 12, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  23 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  24 | Tensor<[1, 12, 14, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  25 | Tensor<[1, 12, 1500, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  26 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  27 | Tensor<[1, 12, 16, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 3        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  28 | Tensor<[1, 12, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  29 | Tensor<[1, 12, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  30 | Tensor<[1, 12, 201, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  31 | Tensor<[1, 12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  32 | Tensor<[1, 12, 25, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  33 | Tensor<[1, 12, 4, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  34 | Tensor<[1, 12, 45, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  35 | Tensor<[1, 12, 46, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  36 | Tensor<[1, 12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  37 | Tensor<[1, 12, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | None     | N/A                 | N/A          | N/A               | N/A                |
|  38 | Tensor<[1, 12, 7, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  39 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  40 | Tensor<[1, 12, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  41 | Tensor<[1, 12, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  42 | Tensor<[1, 12, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  43 | Tensor<[1, 1200, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  44 | Tensor<[1, 128, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  45 | Tensor<[1, 128, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  46 | Tensor<[1, 1280, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  47 | Tensor<[1, 1370, 1, 3, 1280]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2 | None     | N/A                 | N/A          | N/A               | N/A                |
|  48 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  49 | Tensor<[1, 144, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  50 | Tensor<[1, 15, 6, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  51 | Tensor<[1, 1500, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  52 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  53 | Tensor<[1, 16, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  54 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  55 | Tensor<[1, 16, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  56 | Tensor<[1, 16, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  57 | Tensor<[1, 16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  58 | Tensor<[1, 16, 197, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  59 | Tensor<[1, 16, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  60 | Tensor<[1, 16, 256, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | N/A                 | N/A          | N/A               | N/A                |
|  61 | Tensor<[1, 16, 5, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  62 | Tensor<[1, 16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  63 | Tensor<[1, 16, 6, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  64 | Tensor<[1, 16, 64, 197]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  65 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  66 | Tensor<[1, 16, 9, 128]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  67 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | N/A                 | N/A          | N/A               | N/A                |
|  68 | Tensor<[1, 16, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  69 | Tensor<[1, 16, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2    | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  70 | Tensor<[1, 16, s10 + 1, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2 | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  71 | Tensor<[1, 160, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  72 | Tensor<[1, 16384, 128]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  73 | Tensor<[1, 16384, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  74 | Tensor<[1, 16384, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  75 | Tensor<[1, 19, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  76 | Tensor<[1, 192, 1344]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  77 | Tensor<[1, 19200, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  78 | Tensor<[1, 196, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  79 | Tensor<[1, 196, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  80 | Tensor<[1, 197, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2  | None     | N/A                 | N/A          | N/A               | N/A                |
|  81 | Tensor<[1, 197, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | None     | N/A                 | N/A          | N/A               | N/A                |
|  82 | Tensor<[1, 197, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  83 | Tensor<[1, 197, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  84 | Tensor<[1, 2, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  85 | Tensor<[1, 2, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  86 | Tensor<[1, 2, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  87 | Tensor<[1, 2048, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  88 | Tensor<[1, 24, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  89 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  90 | Tensor<[1, 24, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  91 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
|  92 | Tensor<[1, 24, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  93 | Tensor<[1, 24576]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0             | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  94 | Tensor<[1, 256, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  95 | Tensor<[1, 256, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
|  96 | Tensor<[1, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
|  97 | Tensor<[1, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
|  98 | Tensor<[1, 256, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
|  99 | Tensor<[1, 256, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 100 | Tensor<[1, 3, 1445, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 101 | Tensor<[1, 300, 2048]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 102 | Tensor<[1, 32, 16, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 103 | Tensor<[1, 32, 16384]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 104 | Tensor<[1, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 105 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 106 | Tensor<[1, 32, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 107 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 108 | Tensor<[1, 32, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 109 | Tensor<[1, 320, 1200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 110 | Tensor<[1, 4, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 111 | Tensor<[1, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 112 | Tensor<[1, 4096, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 113 | Tensor<[1, 4096, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 114 | Tensor<[1, 4150, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 115 | Tensor<[1, 4800, 512]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 116 | Tensor<[1, 49, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 117 | Tensor<[1, 5, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 118 | Tensor<[1, 5, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 119 | Tensor<[1, 5, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 120 | Tensor<[1, 50, 1, 3, 1024]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2   | None     | N/A                 | N/A          | N/A               | N/A                |
| 121 | Tensor<[1, 50, 1, 3, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = -2    | None     | N/A                 | N/A          | N/A               | N/A                |
| 122 | Tensor<[1, 50, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 123 | Tensor<[1, 50, 12, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 124 | Tensor<[1, 50, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 125 | Tensor<[1, 512, 300]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 126 | Tensor<[1, 512, 4800]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 127 | Tensor<[1, 59, 16, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 128 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 129 | Tensor<[1, 6, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 130 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 131 | Tensor<[1, 6, 15, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 132 | Tensor<[1, 6, 17, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 133 | Tensor<[1, 6, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 134 | Tensor<[1, 6, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 135 | Tensor<[1, 64, 19200]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 136 | Tensor<[1, 64, 4096]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 137 | Tensor<[1, 64, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 138 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 139 | Tensor<[1, 64, 9, 64]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 140 | Tensor<[1, 640, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 141 | Tensor<[1, 7, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 142 | Tensor<[1, 7, 71, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 143 | Tensor<[1, 768, 192]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 144 | Tensor<[1, 768, 196]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 145 | Tensor<[1, 768, 49]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | None     | N/A                 | N/A          | N/A               | N/A                |
| 146 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 147 | Tensor<[1, 8, 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 148 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 149 | Tensor<[1, 8, 10, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 150 | Tensor<[1, 8, 1024, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 151 | Tensor<[1, 8, 2, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 152 | Tensor<[1, 8, 2048, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2     | Done     | N/A                 | N/A          | N/A               | N/A                |
| 153 | Tensor<[1, 8, 256, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 154 | Tensor<[1, 8, 256, 32]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 155 | Tensor<[1, 8, 300, 64]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 156 | Tensor<[1, 8, 32, 256]> self = ?,<br>int dim0 = -1,<br>int dim1 = -2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 157 | Tensor<[1, 8, 4096, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 158 | Tensor<[1, 8, 64, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 159 | Tensor<[1, 8, s0 + 1, 64]> self = ?,<br>int dim0 = 3,<br>int dim1 = 2     | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 160 | Tensor<[1, 80, 96]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 161 | Tensor<[1, 9, 8, 160]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 162 | Tensor<[1, 9, 8, 40]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 163 | Tensor<[1, 9, 8, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 164 | Tensor<[1, 96, 80]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 165 | Tensor<[1, 96, 80]> self = ?,<br>int dim0 = 2,<br>int dim1 = 1            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 166 | Tensor<[100, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 167 | Tensor<[12, 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 168 | Tensor<[12, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | None     | N/A                 | N/A          | N/A               | N/A                |
| 169 | Tensor<[12, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 170 | Tensor<[12, 2, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 171 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 172 | Tensor<[12, 24, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 173 | Tensor<[12, 50, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 174 | Tensor<[12, 50, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 175 | Tensor<[12, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | None     | N/A                 | N/A          | N/A               | N/A                |
| 176 | Tensor<[12, 64, 50]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 177 | Tensor<[12, s0 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 178 | Tensor<[12, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 179 | Tensor<[12, s2 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 180 | Tensor<[12, s4 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 181 | Tensor<[12, s6 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 182 | Tensor<[12, s8 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 183 | Tensor<[1370, 1, 1280]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 184 | Tensor<[1370, 16, 80]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 185 | Tensor<[16, 19, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 186 | Tensor<[16, 197, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 187 | Tensor<[16, 197, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 188 | Tensor<[16, 59, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 189 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 190 | Tensor<[16, 6, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 191 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 192 | Tensor<[16, 6, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 193 | Tensor<[16, 60, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 194 | Tensor<[16, 64, 197]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 195 | Tensor<[16, 64, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | None     | N/A                 | N/A          | N/A               | N/A                |
| 196 | Tensor<[16, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2            | Done     | N/A                 | N/A          | N/A               | N/A                |
| 197 | Tensor<[16, 7, 7]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2             | None     | N/A                 | N/A          | N/A               | N/A                |
| 198 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 199 | Tensor<[16, 8, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 200 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 201 | Tensor<[16, 8, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 202 | Tensor<[16, s10 + 1, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2      | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 203 | Tensor<[197, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 204 | Tensor<[197, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 205 | Tensor<[197, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 206 | Tensor<[197, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 207 | Tensor<[2, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 208 | Tensor<[2, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 209 | Tensor<[2, 4096, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 210 | Tensor<[2, 4096, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 211 | Tensor<[2, 7, 8, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 212 | Tensor<[2, 8, 7, 64]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 213 | Tensor<[24, 12, 24]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 214 | Tensor<[24, 24, 64]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 215 | Tensor<[262, 768]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1             | Done     | N/A                 | N/A          | N/A               | N/A                |
| 216 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 217 | Tensor<[4, 12, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 218 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 219 | Tensor<[4, 12, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 220 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 221 | Tensor<[4, 16, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 222 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 223 | Tensor<[4, 16, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 224 | Tensor<[5, 1024, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2         | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 225 | Tensor<[5, 1024, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 226 | Tensor<[5, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 227 | Tensor<[5, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 228 | Tensor<[50, 1, 1024]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0          | Done     | N/A                 | N/A          | N/A               | N/A                |
| 229 | Tensor<[50, 1, 768]> self = ?,<br>int dim0 = 1,<br>int dim1 = 0           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 230 | Tensor<[50, 12, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 231 | Tensor<[50, 16, 64]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 232 | Tensor<[6, 100, 1, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2       | Done     | N/A                 | N/A          | N/A               | N/A                |
| 233 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 234 | Tensor<[64, 3, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 235 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 236 | Tensor<[64, 3, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 237 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 238 | Tensor<[64, 4, 49, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 239 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1      | Done     | N/A                 | N/A          | N/A               | N/A                |
| 240 | Tensor<[64, 4, 64, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2        | Done     | N/A                 | N/A          | N/A               | N/A                |
| 241 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 242 | Tensor<[8, 100, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 243 | Tensor<[8, 256, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2          | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 244 | Tensor<[8, 256, 32]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 245 | Tensor<[8, 32, 256]> self = ?,<br>int dim0 = 1,<br>int dim1 = 2           | Unknown  | N/A                 | N/A          | N/A               | N/A                |
| 246 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = -2,<br>int dim1 = -1         | Done     | N/A                 | N/A          | N/A               | N/A                |
| 247 | Tensor<[8, 920, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |
| 248 | Tensor<[920, 8, 32]> self = ?,<br>int dim0 = 0,<br>int dim1 = 1           | Done     | N/A                 | N/A          | N/A               | N/A                |

