### aten.permute.default
|     | ATen Input Variations                                                           | Status   | Isolated   | PCC   | Host   |
|----:|:--------------------------------------------------------------------------------|:---------|:-----------|:------|:-------|
|   0 | Tensor<[1, 1, 1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Unknown    | N/A   | N/A    |
|   1 | Tensor<[1, 1, 1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|   2 | Tensor<[1, 1, 1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Unknown    | N/A   | N/A    |
|   3 | Tensor<[1, 1, 1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|   4 | Tensor<[1, 1, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
|   5 | Tensor<[1, 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Done     | Unknown    | N/A   | N/A    |
|   6 | Tensor<[1, 1, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
|   7 | Tensor<[1, 1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|   8 | Tensor<[1, 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Done     | Unknown    | N/A   | N/A    |
|   9 | Tensor<[1, 1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|  10 | Tensor<[1, 1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  11 | Tensor<[1, 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Done     | Unknown    | N/A   | N/A    |
|  12 | Tensor<[1, 1, 7, 1, 7, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Unknown    | N/A   | N/A    |
|  13 | Tensor<[1, 1, 7, 1, 7, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  14 | Tensor<[1, 1, 8, 1, 8, 1024]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]  | None     | Unknown    | N/A   | N/A    |
|  15 | Tensor<[1, 1, 8, 1, 8, 768]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  16 | Tensor<[1, 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Done     | Unknown    | N/A   | N/A    |
|  17 | Tensor<[1, 10, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  18 | Tensor<[1, 1024, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  19 | Tensor<[1, 1024, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  20 | Tensor<[1, 1024, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  21 | Tensor<[1, 1024, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  22 | Tensor<[1, 1024, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  23 | Tensor<[1, 12, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
|  24 | Tensor<[1, 12, 10, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  25 | Tensor<[1, 12, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  26 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  27 | Tensor<[1, 12, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  28 | Tensor<[1, 12, 25, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  29 | Tensor<[1, 12, 45, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Unknown    | N/A   | N/A    |
|  30 | Tensor<[1, 12, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  31 | Tensor<[1, 12, 7, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Unknown    | N/A   | N/A    |
|  32 | Tensor<[1, 120, 160, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Done     | Unknown    | N/A   | N/A    |
|  33 | Tensor<[1, 1200, 320]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  34 | Tensor<[1, 1200, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  35 | Tensor<[1, 128, 128, 32]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Done     | Unknown    | N/A   | N/A    |
|  36 | Tensor<[1, 128, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  37 | Tensor<[1, 128, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Unknown    | N/A   | N/A    |
|  38 | Tensor<[1, 128, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Unknown    | N/A   | N/A    |
|  39 | Tensor<[1, 1280, 1369]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Unknown    | N/A   | N/A    |
|  40 | Tensor<[1, 1280, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Unknown  | Unknown    | N/A   | N/A    |
|  41 | Tensor<[1, 1280, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Unknown  | Unknown    | N/A   | N/A    |
|  42 | Tensor<[1, 14, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  43 | Tensor<[1, 1445, 3, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  44 | Tensor<[1, 15, 20, 512]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
|  45 | Tensor<[1, 16, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
|  46 | Tensor<[1, 16, 1370, 80]> self = ?,<br>List[int] dims = [2, 0, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|  47 | Tensor<[1, 16, 16, 16, 16, 3]> self = ?,<br>List[int] dims = [0, 5, 1, 3, 2, 4] | None     | Unknown    | N/A   | N/A    |
|  48 | Tensor<[1, 16, 16, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
|  49 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  50 | Tensor<[1, 16, 197, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  51 | Tensor<[1, 16, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  52 | Tensor<[1, 16, 32, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  53 | Tensor<[1, 16, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
|  54 | Tensor<[1, 16, 50, 64]> self = ?,<br>List[int] dims = [2, 0, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  55 | Tensor<[1, 160, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  56 | Tensor<[1, 160, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  57 | Tensor<[1, 160, 32, 32]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Unknown    | N/A   | N/A    |
|  58 | Tensor<[1, 16384, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|  59 | Tensor<[1, 16384, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Unknown    | N/A   | N/A    |
|  60 | Tensor<[1, 16384, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  61 | Tensor<[1, 19200, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|  62 | Tensor<[1, 19200, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  63 | Tensor<[1, 197, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  64 | Tensor<[1, 197, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  65 | Tensor<[1, 2, 2, 7, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  66 | Tensor<[1, 2, 2, 7, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  67 | Tensor<[1, 2, 2, 8, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  68 | Tensor<[1, 2, 2, 8, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  69 | Tensor<[1, 2, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  70 | Tensor<[1, 2, 4096, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  71 | Tensor<[1, 2, 4800, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  72 | Tensor<[1, 2, 7, 2, 7, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  73 | Tensor<[1, 2, 7, 2, 7, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  74 | Tensor<[1, 2, 8, 2, 8, 384]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  75 | Tensor<[1, 2, 8, 2, 8, 512]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
|  76 | Tensor<[1, 2048, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]            | Done     | Unknown    | N/A   | N/A    |
|  77 | Tensor<[1, 2048, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  78 | Tensor<[1, 23, 40, 256]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
|  79 | Tensor<[1, 25, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  80 | Tensor<[1, 256, 1, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  81 | Tensor<[1, 256, 1024]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  82 | Tensor<[1, 256, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Done     | Unknown    | N/A   | N/A    |
|  83 | Tensor<[1, 256, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  84 | Tensor<[1, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  85 | Tensor<[1, 256, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                 | Done     | Unknown    | N/A   | N/A    |
|  86 | Tensor<[1, 256, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  87 | Tensor<[1, 256, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  88 | Tensor<[1, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
|  89 | Tensor<[1, 256, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
|  90 | Tensor<[1, 256, 5, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  91 | Tensor<[1, 256, 512]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  92 | Tensor<[1, 256, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
|  93 | Tensor<[1, 256, 8, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  94 | Tensor<[1, 256, 8, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  95 | Tensor<[1, 256, 8, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
|  96 | Tensor<[1, 256, 920]> self = ?,<br>List[int] dims = [2, 0, 1]                   | Done     | Unknown    | N/A   | N/A    |
|  97 | Tensor<[1, 3, 1445, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
|  98 | Tensor<[1, 3, 16, 16, 16, 16]> self = ?,<br>List[int] dims = [0, 2, 4, 3, 5, 1] | None     | Unknown    | N/A   | N/A    |
|  99 | Tensor<[1, 30, 40, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
| 100 | Tensor<[1, 300, 1, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 101 | Tensor<[1, 300, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 102 | Tensor<[1, 300, 5, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 103 | Tensor<[1, 300, 8, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 104 | Tensor<[1, 32, 128, 128]> self = ?,<br>List[int] dims = [0, 2, 3, 1]            | Done     | Unknown    | N/A   | N/A    |
| 105 | Tensor<[1, 32, 16, 96]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Unknown    | N/A   | N/A    |
| 106 | Tensor<[1, 32, 16384]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 107 | Tensor<[1, 32, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 108 | Tensor<[1, 32, 32, 160]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
| 109 | Tensor<[1, 320, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
| 110 | Tensor<[1, 320, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 111 | Tensor<[1, 320, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 112 | Tensor<[1, 4, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 113 | Tensor<[1, 4, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 114 | Tensor<[1, 4, 4, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 115 | Tensor<[1, 4, 4, 7, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 116 | Tensor<[1, 4, 4, 7, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 117 | Tensor<[1, 4, 4, 8, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 118 | Tensor<[1, 4, 4, 8, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 119 | Tensor<[1, 4, 7, 4, 7, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 120 | Tensor<[1, 4, 7, 4, 7, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 121 | Tensor<[1, 4, 8, 4, 8, 192]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 122 | Tensor<[1, 4, 8, 4, 8, 256]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 123 | Tensor<[1, 4, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 124 | Tensor<[1, 4, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 125 | Tensor<[1, 4, 91, 38, 38]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 126 | Tensor<[1, 4096, 2, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 127 | Tensor<[1, 4096, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 128 | Tensor<[1, 4096, 64]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
| 129 | Tensor<[1, 45, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Unknown  | Unknown    | N/A   | N/A    |
| 130 | Tensor<[1, 4800, 128]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 131 | Tensor<[1, 4800, 2, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 132 | Tensor<[1, 49, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 133 | Tensor<[1, 49, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 134 | Tensor<[1, 5, 1024, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 135 | Tensor<[1, 5, 1200, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 136 | Tensor<[1, 5, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Unknown  | Unknown    | N/A   | N/A    |
| 137 | Tensor<[1, 5, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 138 | Tensor<[1, 512, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
| 139 | Tensor<[1, 6, 4, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 140 | Tensor<[1, 6, 4, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 141 | Tensor<[1, 6, 4, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 142 | Tensor<[1, 6, 4, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 143 | Tensor<[1, 6, 4, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 144 | Tensor<[1, 6, 4, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 145 | Tensor<[1, 6, 4, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 146 | Tensor<[1, 6, 91, 1, 1]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 147 | Tensor<[1, 6, 91, 10, 10]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 148 | Tensor<[1, 6, 91, 19, 19]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 149 | Tensor<[1, 6, 91, 2, 2]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 150 | Tensor<[1, 6, 91, 20, 20]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 151 | Tensor<[1, 6, 91, 3, 3]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 152 | Tensor<[1, 6, 91, 5, 5]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 153 | Tensor<[1, 60, 80, 128]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Done     | Unknown    | N/A   | N/A    |
| 154 | Tensor<[1, 64, 256]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 155 | Tensor<[1, 64, 3, 24, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 156 | Tensor<[1, 64, 3, 32, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 157 | Tensor<[1, 64, 300]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 158 | Tensor<[1, 64, 4096]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
| 159 | Tensor<[1, 64, 64, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   | N/A    |
| 160 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Unknown    | N/A   | N/A    |
| 161 | Tensor<[1, 64, 64, 64]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Unknown    | N/A   | N/A    |
| 162 | Tensor<[1, 640, s0, s1]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 163 | Tensor<[1, 640, s1, s2]> self = ?,<br>List[int] dims = [0, 2, 3, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 164 | Tensor<[1, 7, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Unknown    | N/A   | N/A    |
| 165 | Tensor<[1, 7, 7, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Unknown    | N/A   | N/A    |
| 166 | Tensor<[1, 7, 7, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Unknown    | N/A   | N/A    |
| 167 | Tensor<[1, 768, 1500]> self = ?,<br>List[int] dims = [0, 2, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 168 | Tensor<[1, 768, 196]> self = ?,<br>List[int] dims = [0, 2, 1]                   | Done     | Unknown    | N/A   | N/A    |
| 169 | Tensor<[1, 768, 49]> self = ?,<br>List[int] dims = [0, 2, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 170 | Tensor<[1, 8, 2048, 96]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 171 | Tensor<[1, 8, 256, 160]> self = ?,<br>List[int] dims = [0, 2, 1, 3]             | Done     | Unknown    | N/A   | N/A    |
| 172 | Tensor<[1, 8, 256, 32]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 173 | Tensor<[1, 8, 300, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 174 | Tensor<[1, 8, 7, 8, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 175 | Tensor<[1, 8, 7, 8, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Unknown    | N/A   | N/A    |
| 176 | Tensor<[1, 8, 8, 1024]> self = ?,<br>List[int] dims = [0, 3, 1, 2]              | Done     | Unknown    | N/A   | N/A    |
| 177 | Tensor<[1, 8, 8, 7, 7, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 178 | Tensor<[1, 8, 8, 7, 7, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Unknown    | N/A   | N/A    |
| 179 | Tensor<[1, 8, 8, 768]> self = ?,<br>List[int] dims = [0, 3, 1, 2]               | Done     | Unknown    | N/A   | N/A    |
| 180 | Tensor<[1, 8, 8, 8, 8, 128]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]   | None     | Unknown    | N/A   | N/A    |
| 181 | Tensor<[1, 8, 8, 8, 8, 96]> self = ?,<br>List[int] dims = [0, 1, 3, 2, 4, 5]    | None     | Unknown    | N/A   | N/A    |
| 182 | Tensor<[1, 9, 12, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Unknown    | N/A   | N/A    |
| 183 | Tensor<[1, 9, 16, 128]> self = ?,<br>List[int] dims = [0, 2, 1, 3]              | Done     | Unknown    | N/A   | N/A    |
| 184 | Tensor<[1, 9, 16, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Unknown    | N/A   | N/A    |
| 185 | Tensor<[1, 9, 4, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]       | None     | Unknown    | N/A   | N/A    |
| 186 | Tensor<[1, 9, 4, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 187 | Tensor<[1, 9, 4, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 188 | Tensor<[1, 9, 4, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]         | None     | Unknown    | N/A   | N/A    |
| 189 | Tensor<[1, 9, 4, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]           | None     | Unknown    | N/A   | N/A    |
| 190 | Tensor<[1, 9, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 1, 3]               | Done     | Unknown    | N/A   | N/A    |
| 191 | Tensor<[1, 9, 91, 100, 136]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]      | None     | Unknown    | N/A   | N/A    |
| 192 | Tensor<[1, 9, 91, 13, 17]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 193 | Tensor<[1, 9, 91, 25, 34]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 194 | Tensor<[1, 9, 91, 50, 68]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]        | None     | Unknown    | N/A   | N/A    |
| 195 | Tensor<[1, 9, 91, 7, 9]> self = ?,<br>List[int] dims = [0, 3, 4, 1, 2]          | None     | Unknown    | N/A   | N/A    |
| 196 | Tensor<[1, 96, 56, 56]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Unknown    | N/A   | N/A    |
| 197 | Tensor<[1, 96, 64, 64]> self = ?,<br>List[int] dims = [0, 2, 3, 1]              | Done     | Unknown    | N/A   | N/A    |
| 198 | Tensor<[1, s0, s1, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  | Unknown    | N/A   | N/A    |
| 199 | Tensor<[1, s0, s1, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   | N/A    |
| 200 | Tensor<[1, s1, s2, 1280]> self = ?,<br>List[int] dims = [0, 3, 1, 2]            | Unknown  | Unknown    | N/A   | N/A    |
| 201 | Tensor<[1, s1, s2, 320]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   | N/A    |
| 202 | Tensor<[1, s1, s2, 640]> self = ?,<br>List[int] dims = [0, 3, 1, 2]             | Unknown  | Unknown    | N/A   | N/A    |
| 203 | Tensor<[10, 10, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 204 | Tensor<[10, 10, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 205 | Tensor<[10, 10, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 206 | Tensor<[12, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]                  | Done     | Unknown    | N/A   | N/A    |
| 207 | Tensor<[15, 15, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 208 | Tensor<[16, 197, 197]> self = ?,<br>List[int] dims = [1, 2, 0]                  | Done     | Unknown    | N/A   | N/A    |
| 209 | Tensor<[16, 49, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 210 | Tensor<[16, 49, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 211 | Tensor<[16, 64, 3, 6, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 212 | Tensor<[16, 64, 3, 8, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 213 | Tensor<[17, 17, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Unknown  | Unknown    | N/A   | N/A    |
| 214 | Tensor<[197, 197, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 215 | Tensor<[197, 197, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                  | Done     | Unknown    | N/A   | N/A    |
| 216 | Tensor<[2, 2, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Unknown    | N/A   | N/A    |
| 217 | Tensor<[2, 2, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                      | Unknown  | Unknown    | N/A   | N/A    |
| 218 | Tensor<[2, 2, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Unknown    | N/A   | N/A    |
| 219 | Tensor<[2, 2, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                       | Unknown  | Unknown    | N/A   | N/A    |
| 220 | Tensor<[2, 7, 2, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 221 | Tensor<[2, 8, 2, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 222 | Tensor<[4, 49, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 223 | Tensor<[4, 49, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 224 | Tensor<[4, 64, 3, 12, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 225 | Tensor<[4, 64, 3, 16, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 226 | Tensor<[4, 7, 4, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 227 | Tensor<[4, 8, 4, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 228 | Tensor<[49, 49, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 229 | Tensor<[49, 49, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 230 | Tensor<[49, 49, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 231 | Tensor<[49, 49, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 232 | Tensor<[49, 49, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 233 | Tensor<[49, 49, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 234 | Tensor<[49, 49, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 235 | Tensor<[49, 49, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 236 | Tensor<[64, 49, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 237 | Tensor<[64, 49, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 238 | Tensor<[64, 64, 12]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 239 | Tensor<[64, 64, 16]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 240 | Tensor<[64, 64, 24]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 241 | Tensor<[64, 64, 3, 3, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 242 | Tensor<[64, 64, 3, 4, 32]> self = ?,<br>List[int] dims = [2, 0, 3, 1, 4]        | None     | Unknown    | N/A   | N/A    |
| 243 | Tensor<[64, 64, 32]> self = ?,<br>List[int] dims = [2, 0, 1]                    | Done     | Unknown    | N/A   | N/A    |
| 244 | Tensor<[64, 64, 3]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 245 | Tensor<[64, 64, 4]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 246 | Tensor<[64, 64, 6]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 247 | Tensor<[64, 64, 8]> self = ?,<br>List[int] dims = [2, 0, 1]                     | Done     | Unknown    | N/A   | N/A    |
| 248 | Tensor<[8, 7, 8, 7]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 249 | Tensor<[8, 8, 8, 8]> self = ?,<br>List[int] dims = [0, 2, 1, 3]                 | Done     | Unknown    | N/A   | N/A    |
| 250 | Tensor<[s0 + 1, s0 + 1, 12]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   | N/A    |
| 251 | Tensor<[s0 + 1, s0 + 1, 16]> self = ?,<br>List[int] dims = [2, 0, 1]            | Unknown  | Unknown    | N/A   | N/A    |
| 252 | Tensor<[s0 + 1, s0 + 1, 6]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   | N/A    |
| 253 | Tensor<[s0 + 1, s0 + 1, 8]> self = ?,<br>List[int] dims = [2, 0, 1]             | Unknown  | Unknown    | N/A   | N/A    |

