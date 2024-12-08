### aten.select.int
|     | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|----:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 0             | Unknown  | Failed     | N/A   | N/A    |
|   1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 1             | Unknown  | Failed     | N/A   | N/A    |
|   2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2             | Unknown  | Failed     | N/A   | N/A    |
|   3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 3             | Unknown  | Failed     | N/A   | N/A    |
|   4 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | Done     | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0            | Done     | Done       | 1.0   | 1      |
|   8 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | Done     | Done       | 1.0   | 1      |
|   9 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0            | Done     | Done       | 1.0   | 1      |
|  10 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 1      |
|  11 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 1      |
|  12 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 1      |
|  13 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 1      |
|  14 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 1      |
|  15 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 1      |
|  16 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 1      |
|  17 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 1      |
|  18 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 1      |
|  19 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 1      |
|  20 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 1      |
|  21 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 2   | Done     | Done       | 1.0   | 1      |
|  22 | Tensor<[1, 3, 300, 300]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  23 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  24 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  25 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int dim = 0,<br>int index = 0  | Done     | Done       | 1.0   | 0      |
|  26 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  27 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  28 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  29 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 1      |
|  30 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1           | None     | Fallback   | 1.0   | -1     |
|  31 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 1      |
|  32 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 1      |
|  33 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Done       | 1.0   | 1      |
|  34 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1           | Done     | Done       | 1.0   | 1      |
|  35 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | Done     | Done       | 1.0   | 1      |
|  36 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Done       | 1.0   | 1      |
|  37 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | Fallback | Fallback   | 1.0   | -1     |
|  38 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  39 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  40 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  41 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  42 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  43 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  44 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  45 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  46 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  47 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  48 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  49 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  50 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  51 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  52 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  53 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  54 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  55 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  56 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  57 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  58 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  59 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  60 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  61 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  62 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  63 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  64 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  65 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0  | Done     | Done       | 1.0   | 1      |
|  66 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1  | Done     | Done       | 1.0   | 1      |
|  67 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2  | Done     | Done       | 1.0   | 1      |
|  68 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 1      |
|  69 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1   | Done     | Done       | 1.0   | 1      |
|  70 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2   | Done     | Done       | 1.0   | 1      |
|  71 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  72 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  73 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  74 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  75 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  76 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  77 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  78 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  79 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  80 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  81 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  82 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  83 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 1      |
|  84 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1   | Done     | Done       | 1.0   | 1      |
|  85 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2   | Done     | Done       | 1.0   | 1      |
|  86 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0    | Done     | Done       | 1.0   | 1      |
|  87 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1    | Done     | Done       | 1.0   | 1      |
|  88 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2    | Done     | Done       | 1.0   | 1      |
|  89 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  90 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  91 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  92 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  93 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  94 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  95 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  96 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
|  97 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
|  98 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 1      |
|  99 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 1      |
| 100 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 1      |
| 101 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Unknown  | Done       | 1.0   | 1      |
| 102 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Unknown  | Done       | 1.0   | 1      |
| 103 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  | Done       | 1.0   | 1      |
| 104 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Unknown  | Done       | 1.0   | 1      |
| 105 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1    | Done     | Done       | 1.0   | 1      |
| 106 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | Done     | Done       | 1.0   | 1      |
| 107 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Unknown  | Done       | 1.0   | 1      |
| 108 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Unknown  | Done       | 1.0   | 1      |
| 109 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  | Done       | 1.0   | 1      |
| 110 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Unknown  | Done       | 1.0   | 1      |

