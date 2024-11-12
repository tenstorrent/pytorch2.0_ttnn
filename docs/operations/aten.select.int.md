### aten.select.int
|     | ATen Input Variations                                                 | Status   | Isolated   | PCC   |
|----:|:----------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 0             | Unknown  | Unknown    | N/A   |
|   1 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 1             | Unknown  | Unknown    | N/A   |
|   2 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 2             | Unknown  | Unknown    | N/A   |
|   3 | Tensor<[0, 4]> self = ?,<br>int dim = 1,<br>int index = 3             | Unknown  | Unknown    | N/A   |
|   4 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0     | None     | Fallback   | True  |
|   5 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0     | None     | Fallback   | True  |
|   6 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | None     | Fallback   | True  |
|   7 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0            | None     | Fallback   | True  |
|   8 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | None     | Fallback   | True  |
|   9 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0            | None     | Fallback   | True  |
|  10 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0     | None     | Fallback   | True  |
|  11 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | None     | Unknown    | N/A   |
|  12 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0   | None     | Fallback   | True  |
|  13 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1   | None     | Fallback   | True  |
|  14 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | None     | Fallback   | True  |
|  15 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1     | None     | Fallback   | True  |
|  16 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0     | None     | Fallback   | True  |
|  17 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | None     | Fallback   | True  |
|  18 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | None     | Fallback   | True  |
|  19 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0   | None     | Fallback   | True  |
|  20 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 1   | None     | Fallback   | True  |
|  21 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 2   | None     | Fallback   | True  |
|  22 | Tensor<[1, 3, 300, 300]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | Fallback   | True  |
|  23 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | Fallback   | True  |
|  24 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | Fallback   | True  |
|  25 | Tensor<[1, 3, 800, 1066]> self = ?,<br>int dim = 0,<br>int index = 0  | None     | Unknown    | N/A   |
|  26 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | None     | Fallback   | True  |
|  27 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | None     | Fallback   | True  |
|  28 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | None     | Fallback   | True  |
|  29 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | None     | Fallback   | True  |
|  30 | Tensor<[1, 45]> self = ?,<br>int dim = 1,<br>int index = -1           | None     | Fallback   | True  |
|  31 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0      | None     | Fallback   | True  |
|  32 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | None     | Fallback   | True  |
|  33 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Fallback   | True  |
|  34 | Tensor<[1, 59]> self = ?,<br>int dim = 1,<br>int index = -1           | None     | Fallback   | True  |
|  35 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | None     | Fallback   | True  |
|  36 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | None     | Unknown    | N/A   |
|  37 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | None     | Fallback   | True  |
|  38 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  39 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  40 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  41 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   |
|  42 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Unknown    | N/A   |
|  43 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Unknown    | N/A   |
|  44 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  45 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  46 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  47 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  48 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  49 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Unknown    | N/A   |
|  50 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  51 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  52 | Tensor<[3, 1370, 1, 1280]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  53 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  54 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  55 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  56 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   |
|  57 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Unknown    | N/A   |
|  58 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Unknown    | N/A   |
|  59 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  60 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  61 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  62 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  63 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  64 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  65 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0  | None     | Fallback   | True  |
|  66 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1  | None     | Fallback   | True  |
|  67 | Tensor<[3, 197, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2  | None     | Fallback   | True  |
|  68 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | Unknown    | N/A   |
|  69 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1   | None     | Unknown    | N/A   |
|  70 | Tensor<[3, 197, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2   | None     | Unknown    | N/A   |
|  71 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  72 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  73 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  74 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   |
|  75 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Unknown    | N/A   |
|  76 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Unknown    | N/A   |
|  77 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  78 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  79 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  80 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  81 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  82 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  83 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 0   | None     | Fallback   | True  |
|  84 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 1   | None     | Fallback   | True  |
|  85 | Tensor<[3, 50, 1, 1024]> self = ?,<br>int dim = 0,<br>int index = 2   | None     | Fallback   | True  |
|  86 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 0    | None     | Unknown    | N/A   |
|  87 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 1    | None     | Unknown    | N/A   |
|  88 | Tensor<[3, 50, 1, 768]> self = ?,<br>int dim = 0,<br>int index = 2    | None     | Unknown    | N/A   |
|  89 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  90 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  91 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  92 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Unknown    | N/A   |
|  93 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Unknown    | N/A   |
|  94 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Unknown    | N/A   |
|  95 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  96 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
|  97 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
|  98 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | None     | Fallback   | True  |
|  99 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | None     | Fallback   | True  |
| 100 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | None     | Fallback   | True  |
| 101 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Unknown  | Fallback   | True  |
| 102 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Unknown  | Fallback   | True  |
| 103 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  | Fallback   | True  |
| 104 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Unknown  | Fallback   | True  |
| 105 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1    | None     | Fallback   | True  |
| 106 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | None     | Fallback   | True  |
| 107 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Unknown  | Fallback   | True  |
| 108 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Unknown  | Fallback   | True  |
| 109 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Unknown  | Fallback   | True  |
| 110 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Unknown  | Fallback   | True  |

