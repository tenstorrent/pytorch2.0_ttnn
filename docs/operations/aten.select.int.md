### aten.select.int
|     | ATen Input Variations                                                 | Status   | Isolated   | PCC   | Host   |
|----:|:----------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 12, 16]> self = ?,<br>int dim = 1,<br>int index = 0     | Unknown  | Done       | 1.0   | 0      |
|   1 | Tensor<[1, 1, 23, 40]> self = ?,<br>int dim = 0,<br>int index = 0     | Done     | Unknown    | N/A   | N/A    |
|   2 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 0,<br>int index = 0        | Unknown  | Unknown    | N/A   | N/A    |
|   3 | Tensor<[1, 1, 51865]> self = ?,<br>int dim = 1,<br>int index = -1     | Unknown  | Done       | 1.0   | 0      |
|   4 | Tensor<[1, 12]> self = ?,<br>int dim = 1,<br>int index = 0            | Unknown  | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1370, 1280]> self = ?,<br>int dim = 1,<br>int index = 0    | Done     | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 16]> self = ?,<br>int dim = 1,<br>int index = 0            | Unknown  | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 197, 1024]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|   8 | Tensor<[1, 197, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 0      |
|   9 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  10 | Tensor<[1, 2, 120, 160]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
|  11 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|  12 | Tensor<[1, 2, 30, 40]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 0      |
|  13 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 0     | Done     | Done       | 1.0   | 0      |
|  14 | Tensor<[1, 2, 60, 80]> self = ?,<br>int dim = 1,<br>int index = 1     | Done     | Done       | 1.0   | 0      |
|  15 | Tensor<[1, 201, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Unknown  | Unknown    | N/A   | N/A    |
|  16 | Tensor<[1, 25, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 0      |
|  17 | Tensor<[1, 257, 768]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
|  18 | Tensor<[1, 2]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  | Unknown    | N/A   | N/A    |
|  19 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  20 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 1   | Done     | Done       | 1.0   | 0      |
|  21 | Tensor<[1, 3, 224, 224]> self = ?,<br>int dim = 1,<br>int index = 2   | Done     | Done       | 1.0   | 0      |
|  22 | Tensor<[1, 3, 300, 300]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  23 | Tensor<[1, 3, 320, 320]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  24 | Tensor<[1, 3, 480, 640]> self = ?,<br>int dim = 0,<br>int index = 0   | Done     | Done       | 1.0   | 0      |
|  25 | Tensor<[1, 3, 720, 1280]> self = ?,<br>int dim = 0,<br>int index = 0  | Done     | Unknown    | N/A   | N/A    |
|  26 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  27 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  28 | Tensor<[1, 32, 16, 3, 96]> self = ?,<br>int dim = 3,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  29 | Tensor<[1, 4251, 192]> self = ?,<br>int dim = 1,<br>int index = 0     | Removed  | Done       | 1.0   | 0      |
|  30 | Tensor<[1, 46]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Unknown    | N/A   | N/A    |
|  31 | Tensor<[1, 50, 1024]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Done       | 1.0   | 0      |
|  32 | Tensor<[1, 50, 768]> self = ?,<br>int dim = 1,<br>int index = 0       | Done     | Done       | 1.0   | 0      |
|  33 | Tensor<[1, 50]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Done       | 1.0   | 0      |
|  34 | Tensor<[1, 51865]> self = ?,<br>int dim = 0,<br>int index = 0         | Unknown  | Unknown    | N/A   | N/A    |
|  35 | Tensor<[1, 5]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  | Done       | 1.0   | 0      |
|  36 | Tensor<[1, 60]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Unknown    | N/A   | N/A    |
|  37 | Tensor<[1, 6]> self = ?,<br>int dim = 1,<br>int index = -1            | Unknown  | Unknown    | N/A   | N/A    |
|  38 | Tensor<[1, 9, 768]> self = ?,<br>int dim = 1,<br>int index = 0        | Done     | Done       | 1.0   | 0      |
|  39 | Tensor<[1, s0, 256]> self = ?,<br>int dim = 0,<br>int index = 0       | Unknown  | Unknown    | N/A   | N/A    |
|  40 | Tensor<[1, s0]> self = ?,<br>int dim = 1,<br>int index = -1           | Unknown  | Unknown    | N/A   | N/A    |
|  41 | Tensor<[16384, 2, 2]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
|  42 | Tensor<[16384, 2, 2]> self = ?,<br>int dim = 1,<br>int index = 1      | Done     | Unknown    | N/A   | N/A    |
|  43 | Tensor<[16384, 2]> self = ?,<br>int dim = -1,<br>int index = 0        | Done     | Unknown    | N/A   | N/A    |
|  44 | Tensor<[16384, 2]> self = ?,<br>int dim = -1,<br>int index = 1        | Done     | Unknown    | N/A   | N/A    |
|  45 | Tensor<[16384, 2]> self = ?,<br>int dim = 1,<br>int index = 0         | Done     | Unknown    | N/A   | N/A    |
|  46 | Tensor<[16384, 2]> self = ?,<br>int dim = 1,<br>int index = 1         | Done     | Unknown    | N/A   | N/A    |
|  47 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 0     | Done     | Unknown    | N/A   | N/A    |
|  48 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 1     | Done     | Unknown    | N/A   | N/A    |
|  49 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 10    | Done     | Unknown    | N/A   | N/A    |
|  50 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 11    | Done     | Unknown    | N/A   | N/A    |
|  51 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 12    | Done     | Unknown    | N/A   | N/A    |
|  52 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 13    | Done     | Unknown    | N/A   | N/A    |
|  53 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 14    | Done     | Unknown    | N/A   | N/A    |
|  54 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 15    | Done     | Unknown    | N/A   | N/A    |
|  55 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 2     | Done     | Unknown    | N/A   | N/A    |
|  56 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 3     | Done     | Unknown    | N/A   | N/A    |
|  57 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 4     | Done     | Unknown    | N/A   | N/A    |
|  58 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 5     | Done     | Unknown    | N/A   | N/A    |
|  59 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 6     | Done     | Unknown    | N/A   | N/A    |
|  60 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 7     | Done     | Unknown    | N/A   | N/A    |
|  61 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 8     | Done     | Unknown    | N/A   | N/A    |
|  62 | Tensor<[16384, 3, 25]> self = ?,<br>int dim = 2,<br>int index = 9     | Done     | Unknown    | N/A   | N/A    |
|  63 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 0      | Done     | Unknown    | N/A   | N/A    |
|  64 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 1      | Done     | Unknown    | N/A   | N/A    |
|  65 | Tensor<[16384, 3, 3]> self = ?,<br>int dim = 1,<br>int index = 2      | Done     | Unknown    | N/A   | N/A    |
|  66 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 0         | Done     | Unknown    | N/A   | N/A    |
|  67 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 1         | Done     | Unknown    | N/A   | N/A    |
|  68 | Tensor<[16384, 3]> self = ?,<br>int dim = 1,<br>int index = 2         | Done     | Unknown    | N/A   | N/A    |
|  69 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 0         | Done     | Unknown    | N/A   | N/A    |
|  70 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 1         | Done     | Unknown    | N/A   | N/A    |
|  71 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 2         | Done     | Unknown    | N/A   | N/A    |
|  72 | Tensor<[16384, 4]> self = ?,<br>int dim = 1,<br>int index = 3         | Done     | Unknown    | N/A   | N/A    |
|  73 | Tensor<[192, 2]> self = ?,<br>int dim = 1,<br>int index = 0           | Unknown  | Unknown    | N/A   | N/A    |
|  74 | Tensor<[1]> self = ?,<br>int dim = 0,<br>int index = 0                | Unknown  | Done       | 1.0   | 0      |
|  75 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  76 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  77 | Tensor<[3, 1, 24, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  78 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  79 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  80 | Tensor<[3, 1, 24, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  81 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  82 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  83 | Tensor<[3, 1, 32, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  84 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  85 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  86 | Tensor<[3, 1, 32, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  87 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  88 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  89 | Tensor<[3, 16, 6, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  90 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  91 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  92 | Tensor<[3, 16, 6, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  93 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  94 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  95 | Tensor<[3, 16, 8, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  96 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
|  97 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
|  98 | Tensor<[3, 16, 8, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
|  99 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 100 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 101 | Tensor<[3, 4, 12, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 102 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 103 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 104 | Tensor<[3, 4, 12, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 105 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 106 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 107 | Tensor<[3, 4, 16, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 108 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 109 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 110 | Tensor<[3, 4, 16, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 111 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 112 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 113 | Tensor<[3, 64, 3, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 114 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 115 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 116 | Tensor<[3, 64, 3, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 117 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 118 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 119 | Tensor<[3, 64, 4, 49, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 120 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 0 | Done     | Done       | 1.0   | 0      |
| 121 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 1 | Done     | Done       | 1.0   | 0      |
| 122 | Tensor<[3, 64, 4, 64, 32]> self = ?,<br>int dim = 0,<br>int index = 2 | Done     | Done       | 1.0   | 0      |
| 123 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Done     | Unknown    | N/A   | N/A    |
| 124 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Done     | Unknown    | N/A   | N/A    |
| 125 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Done     | Unknown    | N/A   | N/A    |
| 126 | Tensor<[3234, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Done     | Unknown    | N/A   | N/A    |
| 127 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 0                | Unknown  | Unknown    | N/A   | N/A    |
| 128 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 1                | Unknown  | Unknown    | N/A   | N/A    |
| 129 | Tensor<[3]> self = ?,<br>int dim = 0,<br>int index = 2                | Unknown  | Unknown    | N/A   | N/A    |
| 130 | Tensor<[6, 1, 100, 4]> self = ?,<br>int dim = 0,<br>int index = -1    | Done     | Done       | 1.0   | 0      |
| 131 | Tensor<[6, 1, 100, 92]> self = ?,<br>int dim = 0,<br>int index = -1   | Done     | Done       | 1.0   | 0      |
| 132 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 0          | Done     | Unknown    | N/A   | N/A    |
| 133 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 1          | Done     | Unknown    | N/A   | N/A    |
| 134 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 2          | Done     | Unknown    | N/A   | N/A    |
| 135 | Tensor<[8732, 4]> self = ?,<br>int dim = 1,<br>int index = 3          | Done     | Unknown    | N/A   | N/A    |

