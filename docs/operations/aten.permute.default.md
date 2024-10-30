### aten.permute.default
|     | ATen Input Variations                                                           | Status   | Isolated   | PCC   |
|----:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|
|   0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|   1 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|   2 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|   3 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|   4 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
|   5 | Tensor<[1, 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | True  |
|   6 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
|   7 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | True  |
|   8 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | True  |
|   9 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   |
|  10 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | True  |
|  11 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | True  |
|  12 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|  13 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  14 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Fallback   | True  |
|  15 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  16 | Tensor<[1, 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | True  |
|  17 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
|  19 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
|  20 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
|  21 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                   | None     | Fallback   | True  |
|  22 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  23 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
|  24 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  25 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  26 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  27 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Done       | True  |
|  28 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  29 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | True  |
|  30 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Done       | True  |
|  31 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
|  32 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Done     | Unknown    | N/A   |
|  33 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   |
|  34 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   |
|  35 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Done     | Done       | True  |
|  36 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   |
|  37 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | True  |
|  38 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Done       | True  |
|  39 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1]                 | None     | Fallback   | True  |
|  40 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Unknown  | Unknown    | N/A   |
|  41 | Tensor<[1, 1280, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Unknown  | Unknown    | N/A   |
|  42 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  43 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  44 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   |
|  45 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
|  46 | Tensor<[1, 16, 1370, 80]> self = ?,<br>List[int] dims = [2, 0, 1, 3]            | Done     | Done       | True  |
|  47 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] dims = [0, 5, 1, 3, 2, 4] | Unknown  | Fallback   | True  |
|  48 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | True  |
|  49 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  50 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Done       | True  |
|  51 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  52 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  53 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
|  54 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Done       | True  |
|  55 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | True  |
|  56 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | True  |
|  57 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Done       | True  |
|  58 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | True  |
|  59 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Done       | True  |
|  60 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
|  61 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | True  |
|  62 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
|  63 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  64 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  65 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  66 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  67 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  68 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  69 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | True  |
|  70 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  71 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   |
|  72 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  73 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  74 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  75 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
|  76 | Tensor<[1, 2048, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Done       | True  |
|  77 | Tensor<[1, 2048, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  78 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | True  |
|  79 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  80 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  81 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | True  |
|  82 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Done       | True  |
|  83 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  84 | Tensor<[1, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | Done       | True  |
|  85 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Unknown  | Done       | True  |
|  86 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  87 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | True  |
|  88 | Tensor<[1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Unknown  | Done       | True  |
|  89 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | True  |
|  90 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  91 | Tensor<[1, 256, 512]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | True  |
|  92 | Tensor<[1, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Unknown  | Done       | True  |
|  93 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  94 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  95 | Tensor<[1, 256, 8, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
|  96 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Done       | True  |
|  97 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
|  98 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | None     | Fallback   | True  |
|  99 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   |
| 100 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
| 101 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   |
| 102 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   |
| 103 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   |
| 104 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Unknown  | Done       | True  |
| 105 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | True  |
| 106 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Unknown  | Done       | True  |
| 107 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | True  |
| 108 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Done       | True  |
| 109 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   |
| 110 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Done       | True  |
| 111 | Tensor<[1, 320, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   |
| 112 | Tensor<[1, 4, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 113 | Tensor<[1, 4, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 114 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Fallback   | True  |
| 115 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 116 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 117 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 118 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 119 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 120 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 121 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 122 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 123 | Tensor<[1, 4, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 124 | Tensor<[1, 4, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 125 | Tensor<[1, 4, 91, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Fallback   | True  |
| 126 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
| 127 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
| 128 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | True  |
| 129 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | True  |
| 130 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   |
| 131 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   |
| 132 | Tensor<[1, 49, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 133 | Tensor<[1, 49, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 134 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
| 135 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   |
| 136 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Done       | True  |
| 137 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Done       | True  |
| 138 | Tensor<[1, 512, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | Done       | True  |
| 139 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 140 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Fallback   | True  |
| 141 | Tensor<[1, 6, 4, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Fallback   | True  |
| 142 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 143 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Fallback   | True  |
| 144 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 145 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Fallback   | True  |
| 146 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 147 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Fallback   | True  |
| 148 | Tensor<[1, 6, 91, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Fallback   | True  |
| 149 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 150 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Fallback   | True  |
| 151 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 152 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Fallback   | True  |
| 153 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   |
| 154 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | True  |
| 155 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 156 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 157 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Done       | True  |
| 158 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Unknown  | Done       | True  |
| 159 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Done       | True  |
| 160 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Unknown  | Done       | True  |
| 161 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | True  |
| 162 | Tensor<[1, 640, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   |
| 163 | Tensor<[1, 640, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   |
| 164 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 165 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | True  |
| 166 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Done       | True  |
| 167 | Tensor<[1, 71, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 168 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Done       | True  |
| 169 | Tensor<[1, 768, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Done       | True  |
| 170 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                    | None     | Fallback   | True  |
| 171 | Tensor<[1, 8, 2048, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
| 172 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Done       | True  |
| 173 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
| 174 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   |
| 175 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 176 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Fallback   | True  |
| 177 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Done       | True  |
| 178 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 179 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Fallback   | True  |
| 180 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Done       | True  |
| 181 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Fallback   | True  |
| 182 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Fallback   | True  |
| 183 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 184 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Done       | True  |
| 185 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 186 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]       | Unknown  | Fallback   | True  |
| 187 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  | Fallback   | True  |
| 188 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  | Fallback   | True  |
| 189 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | Unknown  | Fallback   | True  |
| 190 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | Unknown  | Fallback   | True  |
| 191 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Done       | True  |
| 192 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | Unknown  | Fallback   | True  |
| 193 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Unknown  | Fallback   | True  |
| 194 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Unknown  | Fallback   | True  |
| 195 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | Unknown  | Fallback   | True  |
| 196 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | Unknown  | Fallback   | True  |
| 197 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | True  |
| 198 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Done       | True  |
| 199 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  | Unknown    | N/A   |
| 200 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   |
| 201 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  | Unknown    | N/A   |
| 202 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   |
| 203 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   |
| 204 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 205 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 206 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 207 | Tensor<[12, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]                  | None     | Fallback   | True  |
| 208 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 209 | Tensor<[16, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]                  | None     | Fallback   | True  |
| 210 | Tensor<[16, 49, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 211 | Tensor<[16, 49, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 212 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 213 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 214 | Tensor<[17, 17, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  | Done       | True  |
| 215 | Tensor<[18176, 4544]> self = ?,<br>List[int] dims = [1, 0]                      | Done     | Done       | True  |
| 216 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 217 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Done       | True  |
| 218 | Tensor<[2, 2, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | True  |
| 219 | Tensor<[2, 2, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Done       | True  |
| 220 | Tensor<[2, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | True  |
| 221 | Tensor<[2, 2, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Done       | True  |
| 222 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | None     | Fallback   | True  |
| 223 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | True  |
| 224 | Tensor<[4, 49, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 225 | Tensor<[4, 49, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 226 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 227 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 228 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | None     | Fallback   | True  |
| 229 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | True  |
| 230 | Tensor<[4544, 18176]> self = ?,<br>List[int] dims = [1, 0]                      | Done     | Done       | True  |
| 231 | Tensor<[4544, 4544]> self = ?,<br>List[int] dims = [1, 0]                       | Done     | Done       | True  |
| 232 | Tensor<[4672, 4544]> self = ?,<br>List[int] dims = [1, 0]                       | Done     | Done       | True  |
| 233 | Tensor<[49, 49, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 234 | Tensor<[49, 49, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 235 | Tensor<[49, 49, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 236 | Tensor<[49, 49, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 237 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | None     | Fallback   | True  |
| 238 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 239 | Tensor<[49, 49, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 240 | Tensor<[49, 49, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 241 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 242 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 243 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 244 | Tensor<[64, 64, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 245 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 246 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 247 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Fallback   | True  |
| 248 | Tensor<[64, 64, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Done       | True  |
| 249 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | None     | Fallback   | True  |
| 250 | Tensor<[64, 64, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 251 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 252 | Tensor<[64, 64, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Done       | True  |
| 253 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | None     | Fallback   | True  |
| 254 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Done       | True  |
| 255 | Tensor<[s0 + 1, s0 + 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   |
| 256 | Tensor<[s0 + 1, s0 + 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   |
| 257 | Tensor<[s0 + 1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   |
| 258 | Tensor<[s0 + 1, s0 + 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   |

