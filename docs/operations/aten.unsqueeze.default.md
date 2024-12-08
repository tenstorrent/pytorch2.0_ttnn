### aten.unsqueeze.default
|     | ATen Input Variations                                 | Status   | Isolated   | PCC   | Host   |
|----:|:------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[0]> self = ?,<br>int dim = 1                  | Unknown  | Done       | 1.0   | -1     |
|   1 | Tensor<[1, 1, 1, 16]> self = ?,<br>int dim = 4        | Unknown  | Done       | 1.0   | 0      |
|   2 | Tensor<[1, 1, 10]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|   3 | Tensor<[1, 1, 12]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|   4 | Tensor<[1, 1, 14]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|   5 | Tensor<[1, 1, 15]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|   6 | Tensor<[1, 1, 16]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|   7 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 1           | Unknown  | Done       | 1.0   | 0      |
|   8 | Tensor<[1, 1, 17]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|   9 | Tensor<[1, 1, 19]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  10 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 1            | Done     | Done       | 1.0   | 0      |
|  11 | Tensor<[1, 1, 1]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
|  12 | Tensor<[1, 1, 2048]> self = ?,<br>int dim = 2         | Done     | Done       | 1.0   | 0      |
|  13 | Tensor<[1, 1, 24]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  14 | Tensor<[1, 1, 256]> self = ?,<br>int dim = 2          | Done     | Done       | 1.0   | 0      |
|  15 | Tensor<[1, 1, 25]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  16 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 1            | Unknown  | Done       | 1.0   | 0      |
|  17 | Tensor<[1, 1, 2]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  18 | Tensor<[1, 1, 32]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  19 | Tensor<[1, 1, 45]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  20 | Tensor<[1, 1, 46]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  21 | Tensor<[1, 1, 59]> self = ?,<br>int dim = 2           | Done     | Done       | 1.0   | 0      |
|  22 | Tensor<[1, 1, 5]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  23 | Tensor<[1, 1, 60]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  24 | Tensor<[1, 1, 6]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  25 | Tensor<[1, 1, 7]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
|  26 | Tensor<[1, 1, 8]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
|  27 | Tensor<[1, 1, 9]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
|  28 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 1       | Unknown  | Unknown    | N/A   | N/A    |
|  29 | Tensor<[1, 1, s0 + 1]> self = ?,<br>int dim = 2       | Unknown  | Unknown    | N/A   | N/A    |
|  30 | Tensor<[1, 1, s10 + 1]> self = ?,<br>int dim = 2      | Unknown  | Unknown    | N/A   | N/A    |
|  31 | Tensor<[1, 1024]> self = ?,<br>int dim = 1            | Done     | Done       | 1.0   | 0      |
|  32 | Tensor<[1, 10]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  33 | Tensor<[1, 120, 160]> self = ?,<br>int dim = 1        | Done     | Done       | 1.0   | 0      |
|  34 | Tensor<[1, 1280, 1]> self = ?,<br>int dim = 3         | Unknown  | Done       | 1.0   | 0      |
|  35 | Tensor<[1, 1280]> self = ?,<br>int dim = 2            | Unknown  | Done       | 1.0   | 0      |
|  36 | Tensor<[1, 12]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  37 | Tensor<[1, 14]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  38 | Tensor<[1, 15]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  39 | Tensor<[1, 17]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | 0      |
|  40 | Tensor<[1, 19, 19]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  41 | Tensor<[1, 192]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
|  42 | Tensor<[1, 19]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  43 | Tensor<[1, 1]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
|  44 | Tensor<[1, 1]> self = ?,<br>int dim = 2               | Done     | Done       | 1.0   | 0      |
|  45 | Tensor<[1, 2048, 2048]> self = ?,<br>int dim = 1      | Done     | Done       | 1.0   | 0      |
|  46 | Tensor<[1, 2048]> self = ?,<br>int dim = 1            | Done     | Done       | 1.0   | 0      |
|  47 | Tensor<[1, 224, 224]> self = ?,<br>int dim = 1        | Done     | Done       | 1.0   | 0      |
|  48 | Tensor<[1, 23, 40]> self = ?,<br>int dim = 3          | Done     | Done       | 1.0   | 0      |
|  49 | Tensor<[1, 24]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  50 | Tensor<[1, 256]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
|  51 | Tensor<[1, 25]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  52 | Tensor<[1, 2]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
|  53 | Tensor<[1, 30, 40]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  54 | Tensor<[1, 32, 32]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  55 | Tensor<[1, 320, 1]> self = ?,<br>int dim = 3          | Unknown  | Done       | 1.0   | 0      |
|  56 | Tensor<[1, 320]> self = ?,<br>int dim = 2             | Unknown  | Done       | 1.0   | 0      |
|  57 | Tensor<[1, 32]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  58 | Tensor<[1, 384, 512]> self = ?,<br>int dim = 1        | Done     | Done       | 1.0   | 0      |
|  59 | Tensor<[1, 45, 45]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  60 | Tensor<[1, 45]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  61 | Tensor<[1, 46]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | 0      |
|  62 | Tensor<[1, 5, 1, 16]> self = ?,<br>int dim = 4        | Unknown  | Done       | 1.0   | 0      |
|  63 | Tensor<[1, 5, 16]> self = ?,<br>int dim = 2           | Unknown  | Done       | 1.0   | 0      |
|  64 | Tensor<[1, 512]> self = ?,<br>int dim = 2             | Done     | Done       | 1.0   | 0      |
|  65 | Tensor<[1, 59, 59]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  66 | Tensor<[1, 59]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
|  67 | Tensor<[1, 5]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
|  68 | Tensor<[1, 60, 80]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
|  69 | Tensor<[1, 60]> self = ?,<br>int dim = 1              | Unknown  | Done       | 1.0   | 0      |
|  70 | Tensor<[1, 640, 1]> self = ?,<br>int dim = 3          | Unknown  | Done       | 1.0   | 0      |
|  71 | Tensor<[1, 640]> self = ?,<br>int dim = 2             | Unknown  | Done       | 1.0   | 0      |
|  72 | Tensor<[1, 64]> self = ?,<br>int dim = 2              | Done     | Done       | 1.0   | 0      |
|  73 | Tensor<[1, 6]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
|  74 | Tensor<[1, 7, 64]> self = ?,<br>int dim = 1           | Done     | Done       | 1.0   | 0      |
|  75 | Tensor<[1, 7, 7]> self = ?,<br>int dim = 1            | Done     | Done       | 1.0   | 0      |
|  76 | Tensor<[1, 720, 1280]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
|  77 | Tensor<[1, 768]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
|  78 | Tensor<[1, 7]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
|  79 | Tensor<[1, 8]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
|  80 | Tensor<[1, 9]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
|  81 | Tensor<[1, s0 + 1]> self = ?,<br>int dim = 1          | Unknown  | Unknown    | N/A   | N/A    |
|  82 | Tensor<[1, s10 + 1]> self = ?,<br>int dim = 1         | Unknown  | Unknown    | N/A   | N/A    |
|  83 | Tensor<[100, 256]> self = ?,<br>int dim = 1           | Done     | Done       | 1.0   | 0      |
|  84 | Tensor<[100]> self = ?,<br>int dim = -1               | Done     | Done       | 1.0   | 0      |
|  85 | Tensor<[10]> self = ?,<br>int dim = 0                 | Done     | Done       | 1.0   | 0      |
|  86 | Tensor<[10]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
|  87 | Tensor<[12, 1, 1]> self = ?,<br>int dim = 0           | Done     | Done       | 1.0   | 0      |
|  88 | Tensor<[12, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
|  89 | Tensor<[12, 197, 197]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
|  90 | Tensor<[12, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
|  91 | Tensor<[12, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
|  92 | Tensor<[12, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
|  93 | Tensor<[12, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
|  94 | Tensor<[120]> self = ?,<br>int dim = 1                | Done     | Done       | 1.0   | 0      |
|  95 | Tensor<[128]> self = ?,<br>int dim = 1                | Done     | Done       | 1.0   | 0      |
|  96 | Tensor<[12]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
|  97 | Tensor<[1370, 1, 3, 1280]> self = ?,<br>int dim = 0   | Done     | Done       | 1.0   | 0      |
|  98 | Tensor<[14]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
|  99 | Tensor<[15]> self = ?,<br>int dim = 0                 | Done     | Done       | 1.0   | 0      |
| 100 | Tensor<[15]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 101 | Tensor<[16, 1, 1]> self = ?,<br>int dim = 0           | Done     | Done       | 1.0   | 0      |
| 102 | Tensor<[16, 1, 49, 49]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
| 103 | Tensor<[16, 1, 64, 64]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
| 104 | Tensor<[16, 10, 10]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 105 | Tensor<[16, 197, 197]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
| 106 | Tensor<[16, 2, 2]> self = ?,<br>int dim = 0           | Unknown  | Done       | 1.0   | 0      |
| 107 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 108 | Tensor<[16, 49, 49]> self = ?,<br>int dim = 1         | Done     | Done       | 1.0   | 0      |
| 109 | Tensor<[16, 49]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
| 110 | Tensor<[16, 49]> self = ?,<br>int dim = 2             | Done     | Done       | 1.0   | 0      |
| 111 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 112 | Tensor<[16, 64, 64]> self = ?,<br>int dim = 1         | Done     | Done       | 1.0   | 0      |
| 113 | Tensor<[16, 64]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
| 114 | Tensor<[16, 64]> self = ?,<br>int dim = 2             | Done     | Done       | 1.0   | 0      |
| 115 | Tensor<[16, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0 | Unknown  | Unknown    | N/A   | N/A    |
| 116 | Tensor<[160]> self = ?,<br>int dim = 0                | Done     | Done       | 1.0   | 0      |
| 117 | Tensor<[16]> self = ?,<br>int dim = -1                | Unknown  | Done       | 1.0   | 0      |
| 118 | Tensor<[16]> self = ?,<br>int dim = 1                 | Removed  | Done       | 1.0   | 0      |
| 119 | Tensor<[17]> self = ?,<br>int dim = 0                 | Unknown  | Done       | 1.0   | 0      |
| 120 | Tensor<[17]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | 0      |
| 121 | Tensor<[19, 19]> self = ?,<br>int dim = 0             | Done     | Done       | 1.0   | 0      |
| 122 | Tensor<[197, 1, 3, 1024]> self = ?,<br>int dim = 0    | Done     | Done       | 1.0   | 0      |
| 123 | Tensor<[197, 1, 3, 768]> self = ?,<br>int dim = 0     | Done     | Done       | 1.0   | 0      |
| 124 | Tensor<[19]> self = ?,<br>int dim = 0                 | Done     | Done       | 1.0   | 0      |
| 125 | Tensor<[1]> self = ?,<br>int dim = 0                  | Done     | Done       | 1.0   | 0      |
| 126 | Tensor<[1]> self = ?,<br>int dim = 1                  | Done     | Done       | 1.0   | 0      |
| 127 | Tensor<[2*s0]> self = ?,<br>int dim = -1              | Unknown  | Unknown    | N/A   | N/A    |
| 128 | Tensor<[2*s1]> self = ?,<br>int dim = -1              | Unknown  | Unknown    | N/A   | N/A    |
| 129 | Tensor<[2, 1, 7]> self = ?,<br>int dim = 2            | Done     | Done       | 1.0   | 0      |
| 130 | Tensor<[2, 7]> self = ?,<br>int dim = 1               | Done     | Done       | 1.0   | 0      |
| 131 | Tensor<[2048, 2048]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 132 | Tensor<[23]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 133 | Tensor<[24, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 134 | Tensor<[24, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 135 | Tensor<[240]> self = ?,<br>int dim = 1                | None     | Fallback   | 1.0   | -1     |
| 136 | Tensor<[24]> self = ?,<br>int dim = 0                 | Removed  | Done       | 1.0   | 0      |
| 137 | Tensor<[24]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 138 | Tensor<[25]> self = ?,<br>int dim = 1                 | Unknown  | Done       | 1.0   | 0      |
| 139 | Tensor<[28]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 140 | Tensor<[2]> self = ?,<br>int dim = 0                  | Unknown  | Done       | 1.0   | 0      |
| 141 | Tensor<[2]> self = ?,<br>int dim = 1                  | Unknown  | Done       | 1.0   | 0      |
| 142 | Tensor<[3, 1]> self = ?,<br>int dim = 2               | Done     | Done       | 1.0   | 0      |
| 143 | Tensor<[3, 320, 320]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | 0      |
| 144 | Tensor<[3, 480, 640]> self = ?,<br>int dim = 0        | Done     | Done       | 1.0   | 0      |
| 145 | Tensor<[3, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 146 | Tensor<[3, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 147 | Tensor<[300]> self = ?,<br>int dim = 1                | None     | Fallback   | 1.0   | -1     |
| 148 | Tensor<[30]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 149 | Tensor<[32, 32]> self = ?,<br>int dim = 0             | Done     | Done       | 1.0   | 0      |
| 150 | Tensor<[32, 49, 49]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 151 | Tensor<[32, 64, 64]> self = ?,<br>int dim = 0         | Done     | Done       | 1.0   | 0      |
| 152 | Tensor<[320]> self = ?,<br>int dim = 1                | None     | Fallback   | 1.0   | -1     |
| 153 | Tensor<[3234]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
| 154 | Tensor<[32]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 155 | Tensor<[32]> self = ?,<br>int dim = 0                 | Removed  | Done       | 1.0   | 0      |
| 156 | Tensor<[3]> self = ?,<br>int dim = 1                  | Done     | Done       | 1.0   | 0      |
| 157 | Tensor<[4, 1, 49, 49]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
| 158 | Tensor<[4, 1, 64, 64]> self = ?,<br>int dim = 0       | Done     | Done       | 1.0   | 0      |
| 159 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 160 | Tensor<[4, 49, 49]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
| 161 | Tensor<[4, 49]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
| 162 | Tensor<[4, 49]> self = ?,<br>int dim = 2              | Done     | Done       | 1.0   | 0      |
| 163 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 164 | Tensor<[4, 64, 64]> self = ?,<br>int dim = 1          | Done     | Done       | 1.0   | 0      |
| 165 | Tensor<[4, 64]> self = ?,<br>int dim = 1              | Done     | Done       | 1.0   | 0      |
| 166 | Tensor<[4, 64]> self = ?,<br>int dim = 2              | Done     | Done       | 1.0   | 0      |
| 167 | Tensor<[45, 45]> self = ?,<br>int dim = 0             | Done     | Done       | 1.0   | 0      |
| 168 | Tensor<[480]> self = ?,<br>int dim = 1                | Done     | Done       | 1.0   | 0      |
| 169 | Tensor<[50, 1, 3, 1024]> self = ?,<br>int dim = 0     | Done     | Done       | 1.0   | 0      |
| 170 | Tensor<[50, 1, 3, 768]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
| 171 | Tensor<[50]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 172 | Tensor<[56]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 173 | Tensor<[59, 59]> self = ?,<br>int dim = 0             | Done     | Done       | 1.0   | 0      |
| 174 | Tensor<[6, 1, 1]> self = ?,<br>int dim = 0            | Done     | Done       | 1.0   | 0      |
| 175 | Tensor<[6, 15, 15]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 176 | Tensor<[6, 17, 17]> self = ?,<br>int dim = 0          | Unknown  | Done       | 1.0   | 0      |
| 177 | Tensor<[6, 2, 2]> self = ?,<br>int dim = 0            | Unknown  | Done       | 1.0   | 0      |
| 178 | Tensor<[6, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 179 | Tensor<[6, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 180 | Tensor<[6, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0  | Unknown  | Unknown    | N/A   | N/A    |
| 181 | Tensor<[60]> self = ?,<br>int dim = 1                 | Done     | Done       | 1.0   | 0      |
| 182 | Tensor<[64, 1, 49, 49]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
| 183 | Tensor<[64, 1, 64, 64]> self = ?,<br>int dim = 0      | Done     | Done       | 1.0   | 0      |
| 184 | Tensor<[64, 49, 49]> self = ?,<br>int dim = 1         | Done     | Done       | 1.0   | 0      |
| 185 | Tensor<[64, 49]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
| 186 | Tensor<[64, 49]> self = ?,<br>int dim = 2             | Done     | Done       | 1.0   | 0      |
| 187 | Tensor<[64, 64, 64]> self = ?,<br>int dim = 1         | Done     | Done       | 1.0   | 0      |
| 188 | Tensor<[64, 64]> self = ?,<br>int dim = 1             | Done     | Done       | 1.0   | 0      |
| 189 | Tensor<[64, 64]> self = ?,<br>int dim = 2             | Done     | Done       | 1.0   | 0      |
| 190 | Tensor<[64]> self = ?,<br>int dim = -1                | Done     | Done       | 1.0   | 0      |
| 191 | Tensor<[64]> self = ?,<br>int dim = 0                 | Done     | Done       | 1.0   | 0      |
| 192 | Tensor<[7, 7]> self = ?,<br>int dim = 0               | Done     | Done       | 1.0   | 0      |
| 193 | Tensor<[7]> self = ?,<br>int dim = -1                 | Done     | Done       | 1.0   | 0      |
| 194 | Tensor<[7]> self = ?,<br>int dim = 0                  | Removed  | Done       | 1.0   | 0      |
| 195 | Tensor<[8, 1, 1]> self = ?,<br>int dim = 0            | Done     | Done       | 1.0   | 0      |
| 196 | Tensor<[8, 10, 10]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 197 | Tensor<[8, 2, 2]> self = ?,<br>int dim = 0            | Unknown  | Done       | 1.0   | 0      |
| 198 | Tensor<[8, 49, 49]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 199 | Tensor<[8, 64, 64]> self = ?,<br>int dim = 0          | Done     | Done       | 1.0   | 0      |
| 200 | Tensor<[8, s0 + 1, s0 + 1]> self = ?,<br>int dim = 0  | Unknown  | Unknown    | N/A   | N/A    |
| 201 | Tensor<[800]> self = ?,<br>int dim = 1                | None     | Fallback   | 1.0   | -1     |
| 202 | Tensor<[8732]> self = ?,<br>int dim = 1               | Unknown  | Done       | 1.0   | 0      |
| 203 | Tensor<[s0 + 1]> self = ?,<br>int dim = 0             | Unknown  | Unknown    | N/A   | N/A    |
| 204 | Tensor<[s0 + 1]> self = ?,<br>int dim = 1             | Unknown  | Unknown    | N/A   | N/A    |

